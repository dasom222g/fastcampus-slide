#!/usr/bin/env python3
"""저장소를 스캔해 강의 제작 현황을 다시 만든다.

만드는 것
  dashboard/index.html          보기용 대시보드
  docs/production-status.md     같은 표의 마크다운본 (커밋 diff로 변화를 읽는다)

읽는 것
  docs/curriculum.md            파트·챕터·클립의 번호·제목·길이 — 여기가 유일한 출처
  dashboard/clips.json          클립별 슬라이드 여부 · 촬영 상태(수기) · 파트별 납기 · 예외
  artifacts/<part>/outputs/     덱 HTML 존재 여부와 실제 장수
  artifacts/<part>/_source/     소스 frontmatter의 슬라이드 장수·상태
  artifacts/<part>/_script/     대본 존재 여부와 대본이 적은 장수
  artifacts/CONFIRMED.md        확정 여부

상태 다섯 가지
  완료      끝났다
  작업중    손대고 있다
  예정      아직 안 했지만 곧 해야 한다 — 앞 공정이 끝났거나 지금 납기의 파트다
  시작전    아직 안 했고 납기도 뒤다 — 지금 신경 쓸 일이 아니다
  해당없음  애초에 그 공정이 없다 (실습 대본, 불필요한 실습자료)

판정 규칙
  실습 클립(슬라이드: false)은 실습자료 제작 → 촬영. 대본은 해당없음, 실습자료도 필요 없으면 해당없음
  제작  덱 없음 → 미착수 / 있고 확정 → 완료 / 있고 확정 아님 → 작업중
  대본  파일 없음 → 미착수 / 있음 → 작업중(초안) / 촬영을 마쳤으면 → 완료
        강사 검수는 촬영 때 이뤄지므로 촬영 완료를 대본 확정으로 본다.
  촬영  clips.json에 적힌 값 그대로 (자동 판정 불가)
  미착수는 두 가지로 갈린다.
    앞 공정이 완료면 → 예정 (제작 완료 → 대본 예정, 대본 완료 → 촬영 예정)
    그 밖에는 파트의 납기를 보고 → 지금 납기면 예정, 아니면 시작전
    이미 완료·작업중인 칸은 건드리지 않는다.
  clips.json에 제작·대본 키를 직접 적으면 그 값이 이긴다.
"""

from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(__file__).resolve().parent

DONE, WIP, DUE, LATER, NA = "완료", "작업중", "예정", "시작전", "해당없음"
MANUAL_STATES = (DONE, WIP, DUE, LATER)
CLS = {DONE: "done", WIP: "wip", DUE: "due", LATER: "later", NA: "na"}
CHIP = {DONE: "완료", WIP: "작업중", DUE: "예정", LATER: "시작전", NA: "—"}

STAGES = (
    ("제작", "슬라이드 또는 실습자료를 만들었는가", "전체 클립"),
    ("대본", "강사 검수까지 끝난 대본이 있는가", "슬라이드 클립"),
    ("촬영", "영상 수록을 마쳤는가", "전체 클립"),
)


# ── 읽기 ────────────────────────────────────────────────────────────


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_curriculum() -> "OrderedDict[tuple[int, str], dict]":
    """`- Ch01-01. 제목 (11분)` 줄을 파트·챕터와 함께 커리큘럼 순서대로 읽는다."""
    text = read(ROOT / "docs" / "curriculum.md")
    if not text:
        die("docs/curriculum.md 를 찾을 수 없다.")

    clips: "OrderedDict[tuple[int, str], dict]" = OrderedDict()
    part_no, part_title, chapter = None, None, None
    for line in text.splitlines():
        m = re.match(r"^##\s+Part\s+(\d+)\.\s*(.+?)\s*$", line)
        if m:
            part_no, part_title, chapter = int(m.group(1)), m.group(2), None
            continue
        m = re.match(r"^###\s+(Chapter\s+\d+\..+?)\s*$", line)
        if m:
            chapter = m.group(1)
            continue
        m = re.match(r"^-\s+(Ch\d{2}-\d{2})\.\s*(.+?)\s*\((\d+)분\)\s*$", line)
        if m and part_no is not None:
            clips[(part_no, m.group(1))] = {
                "파트번호": part_no,
                "파트제목": part_title,
                "챕터": chapter or "",
                "클립": m.group(1),
                "제목": m.group(2),
                "길이": f"{m.group(3)}분",
            }
    if not clips:
        die("커리큘럼에서 클립을 하나도 읽지 못했다. 형식이 바뀌었는지 확인한다.")
    return clips


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.split("#")[0].strip()
    return out


def slide_count(text: str) -> int:
    return len(re.findall(r'<article class="slide[ "]', text))


def declared_count(value: str) -> int | None:
    m = re.search(r"(\d+)\s*장", value or "")
    return int(m.group(1)) if m else None


# ── 납기 ────────────────────────────────────────────────────────────


def delivery_config(manifest: dict) -> tuple[list[dict], dict[str, str], dict[int, int]]:
    """차수와 파트 배정을 검증한다. 이전 파트별 날짜 설정도 호환한다."""
    schedule = {str(k): v for k, v in manifest.get("납기", {}).items()
                if v and not str(k).startswith("_")}
    batches = manifest.get("납품차수", [])
    assigned, seen = {}, set()
    for batch in batches:
        n, deadline = batch.get("차수"), batch.get("납기", "")
        if n not in (1, 2, 3) or n in seen:
            die("납품차수는 1·2·3차를 중복 없이 지정한다.")
        seen.add(n)
        for part in batch.get("파트", []):
            if not isinstance(part, int) or part not in range(1, 11) or part in assigned:
                die("납품차수의 파트는 1~10 중 하나이며 중복 배정할 수 없다.")
            assigned[part] = n
            if deadline:
                schedule[str(part)] = deadline
        if deadline:
            try:
                date.fromisoformat(deadline)
            except (ValueError, TypeError):
                die("납기일은 유효한 YYYY-MM-DD 날짜로 적는다.")
    for deadline in schedule.values():
        try:
            date.fromisoformat(deadline)
        except (ValueError, TypeError):
            die("납기일은 유효한 YYYY-MM-DD 날짜로 적는다.")
    return batches, schedule, assigned


def due_parts(schedule: dict, rows_by_part: dict[int, list[dict]]) -> tuple[set[int], str]:
    """지금 납기에 속한 파트를 고른다.

    남은 일이 있는 파트들의 납기 중 가장 이른 날짜가 '지금 납기'다.
    그 날짜를 가진 파트의 미착수 작업은 예정, 나머지는 시작전이 된다.
    납기가 안 적힌 파트는 항상 시작전이다.
    """
    if not schedule:
        return set(), ""

    open_dates = []
    for part, rows in rows_by_part.items():
        raw = schedule.get(str(part))
        if not raw:
            continue
        if any(r.get("촬영") != DONE for r in rows):
            open_dates.append(raw)
    if not open_dates:
        return set(), ""

    nearest = min(open_dates)
    return {int(p) for p, d in schedule.items() if d == nearest}, nearest


# ── 판정 ────────────────────────────────────────────────────────────


def build_rows() -> tuple[list[dict], list[str], str]:
    curriculum = parse_curriculum()
    try:
        manifest = json.loads(read(ROOT / "dashboard" / "clips.json") or "{}")
    except json.JSONDecodeError as exc:
        die(f"dashboard/clips.json 을 읽을 수 없다 — {exc}")

    entries = {(e.get("파트"), e.get("클립")): e for e in manifest.get("클립", [])}
    if not entries:
        die("dashboard/clips.json 의 「클립」 목록이 비어 있다.")
    for key in entries:
        if key not in curriculum:
            die(f"Part {key[0]} {key[1]} 은 커리큘럼에 없다. clips.json을 확인한다.")

    batches, schedule, assigned = delivery_config(manifest)

    confirmed = read(ROOT / "artifacts" / "CONFIRMED.md")
    rows, warnings = [], []

    for key, meta in curriculum.items():
        part, clip = key
        e = entries.get(key, {})
        row = dict(meta)
        row["슬라이드"] = bool(e.get("슬라이드"))
        row["비고"] = e.get("비고", "")
        row["차수"] = assigned.get(part, 0)
        row["_미착수"] = False

        shot = e.get("촬영", LATER)
        if shot not in MANUAL_STATES:
            die(f"Part {part} {clip} 의 「촬영」 값이 이상하다: {shot!r}")
        if shot in (DUE, LATER):
            row["_미착수"] = True
            shot = None  # 납기를 보고 나중에 채운다

        if not row["슬라이드"]:
            if not e:
                warnings.append(
                    f"Part {part} {clip} — clips.json에 없다. 실습 클립으로 처리했다."
                )
            material = e.get("실습자료", LATER)
            if material not in (*MANUAL_STATES, NA):
                die(f"Part {part} {clip} 의 실습자료 상태가 올바르지 않다.")
            if material in (DUE, LATER):
                material = None
                row["_미착수"] = True
            row.update({"장수": "—", "제작": material, "대본": NA, "촬영": shot})
            row["비고"] = row["비고"] or "실습"
            rows.append(row)
            continue

        slug = e.get("슬러그")
        deck_text = source_text = script_text = ""
        if slug:
            base = ROOT / "artifacts" / f"part{part}"
            deck_text = read(base / "outputs" / f"{slug}.html")
            source_text = read(base / "_source" / f"{slug}.md")
            script_text = read(base / "_script" / f"{slug}.md")

        fm = frontmatter(source_text)
        declared = declared_count(fm.get("슬라이드", ""))
        actual = slide_count(deck_text) if deck_text else None
        count = e.get("장수") or declared or actual
        row["장수"] = f"{count}장" if count else "—"

        made = None
        if deck_text:
            is_confirmed = (slug in confirmed) or ("확정" in fm.get("상태", ""))
            made = DONE if is_confirmed else WIP

        # 대본은 초안이 있어도 강사 검수 전이다. 검수는 촬영 때 이뤄진다.
        scripted = None
        if script_text.strip():
            scripted = DONE if e.get("촬영") == DONE else WIP

        for stage, auto in (("제작", made), ("대본", scripted)):
            value = auto
            if stage in e:
                given = e[stage]
                if given not in MANUAL_STATES:
                    die(f"Part {part} {clip} 의 「{stage}」 값이 이상하다: {given!r}")
                if given != auto:
                    reason = e.get(f"{stage}_사유", "") or f"{stage} 수기 지정"
                    # 제작과 대본에 같은 사유가 걸리면 비고에 두 번 적히지 않게 한다
                    if reason not in row["비고"]:
                        row["비고"] = (
                            row["비고"] + " · " if row["비고"] else ""
                        ) + reason
                value = None if given in (DUE, LATER) else given
            if value is None:
                row["_미착수"] = True
            row[stage] = value

        row["촬영"] = shot

        label = f"Part {part} {clip}"
        if declared and actual and declared != actual:
            warnings.append(f"{label} — 소스는 {declared}장인데 덱은 {actual}장이다.")
        if script_text:
            sc = declared_count(script_text.splitlines()[0])
            ref = declared or actual
            if sc and ref and sc != ref:
                warnings.append(f"{label} — 대본은 {sc}장인데 덱은 {ref}장이다.")
        if slug and not deck_text and row["제작"] not in (None, NA):
            if not e.get("제작_사유"):
                warnings.append(
                    f"{label} — 덱 HTML이 없는데 제작이 {row['제작']}로 적혀 있다."
                )

        rows.append(row)

    # 미착수 칸을 납기에 따라 예정 / 시작전으로 채운다
    by_part: dict[int, list[dict]] = {}
    for r in rows:
        by_part.setdefault(r["파트번호"], []).append(r)
    due, nearest = due_parts(schedule, by_part)

    names = [s for s, _, _ in STAGES]
    for r in rows:
        by_due = DUE if r["파트번호"] in due else LATER
        for i, stage in enumerate(names):
            if r[stage] is not None:
                continue
            # 앞 공정이 끝났으면 이 공정이 바로 다음 차례다 — 납기와 무관하게 예정.
            previous = [r[s] for s in names[:i] if r[s] != NA]
            prev_done = bool(previous) and previous[-1] == DONE
            r[stage] = DUE if prev_done else by_due
        r.pop("_미착수", None)

    return rows, warnings, nearest


def stage_scope(rows: list[dict], stage: str) -> list[dict]:
    """대본은 이론 클립만, 자료 제작과 촬영은 전체 클립이 모집단이다."""
    return [r for r in rows if r[stage] != NA]


# ── 그리기 ──────────────────────────────────────────────────────────


def esc(s: str) -> str:
    return html.escape(s or "")


def chip(state: str, stage: str) -> str:
    title = f"{stage} {state}" if state != NA else f"{stage} 해당없음 — 실습 클립"
    return f'<span class="chip chip--{CLS[state]}" title="{title}">{CHIP[state]}</span>'


def kind_label(theory: bool) -> str:
    # Type uses an open icon + label; colored status pills are reserved for progress.
    drawing = (
        '<path d="M12 6C9 3 5 3 2 4v15c3-1 7-1 10 2 3-3 7-3 10-2V4c-3-1-7-1-10 2Z"/>'
        '<path d="M12 6v15M5 8h3M5 12h3M16 8h3M16 12h3"/>'
        if theory else
        '<path d="m7 7 13 6-6 2-2 6-5-14ZM4 2v3M1 7h3M7 1v3M2 2l2 2"/>'
    )
    kind, label = ("theory", "이론") if theory else ("practice", "실습")
    return (f'<span class="kind kind--{kind}"><svg viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{drawing}</svg>{label}</span>')


HEAD_ROW = """<thead><tr>
            <th scope="col" class="c-clip">클립</th>
            <th scope="col" class="c-title">제목</th>
            <th scope="col" class="c-len">길이</th>
            <th scope="col" class="c-count">유형</th>
            <th scope="col" class="c-stage">자료 제작</th>
            <th scope="col" class="c-stage">대본</th>
            <th scope="col" class="c-stage">촬영</th>
            <th scope="col" class="c-note">비고</th>
          </tr></thead>"""


def render_parts(rows: list[dict], due_note: dict[int, str]) -> str:
    parts: "OrderedDict[int, list[dict]]" = OrderedDict()
    for r in rows:
        parts.setdefault(r["파트번호"], []).append(r)

    out = []
    for no, rs in parts.items():
        slides = [r for r in rs if r["슬라이드"]]
        done = sum(r["촬영"] == DONE for r in rs)
        total = len(rs) or 1
        due = due_note.get(no, "")
        due_html = (
            f'<span class="part__due{"" if not due else " is-due" if due[1] else ""}">{esc(due[0])}</span>'
            if due
            else ""
        )
        out.append(f"""<section class="part" data-part="{no}" data-batch="{rs[0]['차수']}">
        <header class="part__head">
          <h3 class="part__name">Part {no}</h3>
          <span class="part__title">{esc(rs[0]["파트제목"])}</span>
          {due_html}
          <span class="part__tally">{len(rs)}클립</span>
          <span class="part__meter" role="img" aria-label="촬영 {done}/{total} 완료">
            <span class="part__meter-fill" style="width:{done / total * 100:.4f}%"></span>
          </span>
          <span class="part__pct">{done}/{total}</span>
        </header>
        <div class="tablewrap">
        <table class="grid">
          {HEAD_ROW}
          <tbody>""")
        chapter = None
        for r in rs:
            if r["챕터"] != chapter:
                chapter = r["챕터"]
                if chapter:
                    out.append(
                        '<tr class="chap"><th colspan="8" scope="colgroup">'
                        f"{esc(chapter)}</th></tr>"
                    )
            cls = "" if r["슬라이드"] else ' class="row--practice"'
            out.append(f"""<tr{cls} data-key="{no}-{r['클립']}" data-clip>
              <td class="c-clip"><code>{esc(r["클립"])}</code></td>
              <td class="c-title">{esc(r["제목"])}</td>
              <td class="c-len">{esc(r["길이"])}</td>
              <td class="c-count">{kind_label(r["슬라이드"])}</td>
              <td class="c-stage"><small>{'슬라이드' if r['슬라이드'] else '실습자료'}</small>{chip(r["제작"], "자료 제작")}</td>
              <td class="c-stage">{chip(r["대본"], "대본")}</td>
              <td class="c-stage">{chip(r["촬영"], "촬영")}</td>
              <td class="c-note">{esc(r["비고"] if r["비고"] != "실습" else "")}</td>
            </tr>""")
        out.append("          </tbody>\n        </table>\n        </div>\n      </section>")
    return "\n".join(out)


def render_warnings(warnings: list[str]) -> str:
    if not warnings:
        return (
            '<p class="check check--ok"><b>어긋난 곳 없음.</b> '
            "소스의 장수, 덱의 실제 장수, 대본의 장수가 모두 맞는다.</p>"
        )
    items = "".join(f"<li>{esc(w)}</li>" for w in warnings)
    return (
        f'<p class="check check--warn"><b>{len(warnings)}건 확인이 필요하다.</b></p>'
        f'<ul class="checklist">{items}</ul>'
    )


def render_html(rows: list[dict], warnings: list[str], nearest: str, schedule: dict) -> str:
    template = read(SRC / "template.html")
    if not template:
        die("dashboard/src/template.html 을 찾을 수 없다.")
    manifest = json.loads(read(ROOT / "dashboard" / "clips.json"))
    batches, _, _ = delivery_config(manifest)
    payload = json.dumps({"rows": rows, "batches": batches}, ensure_ascii=False).replace("<", "\\u003c")
    return (template.replace("{{DATA}}", payload)
            .replace("{{PARTS}}", render_parts(rows, {}))
            .replace("{{WARNINGS}}", render_warnings(warnings))
            .replace("{{BUILT}}", date.today().isoformat()))


def render_markdown(rows: list[dict], warnings: list[str], nearest: str) -> str:
    slides = [r for r in rows if r["슬라이드"]]
    L = [
        "---",
        "문서: 강의 제작 현황",
        "상태: dashboard/src/build.py 가 생성한다 — 직접 고치지 않는다",
        f"최종 생성: {date.today().isoformat()}",
        "---",
        "",
        "# 강의 제작 현황",
        "",
        f"커리큘럼 {len(rows)}클립의 자료 제작과 촬영을 추적한다. 이론은 슬라이드 → 대본 → 촬영 순이다.",
        f"슬라이드를 만드는 클립은 {len(slides)}개, 나머지 {len(rows) - len(slides)}개는 "
        "실습자료 제작(필요 시) → 촬영으로 진행한다. 대본과 불필요한 실습자료는 **해당없음**이다.",
        "촬영 완료를 클립의 최종 완료로 본다. 해당없음인 공정은 집계에서 제외한다.",
        "",
        "상태는 다섯 가지다 — **완료 · 작업중 · 예정**(앞 공정 완료 또는 지금 납기) **· "
        "시작전**(납기가 뒤) **· 해당없음**.",
        f"지금 납기: {nearest or '날짜 미지정 — 차수별 구분 가능'}",
        "",
        "| 공정 | 모집단 | 완료 | 작업중 | 예정 | 시작전 |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for stage, _, scope in STAGES:
        pool = stage_scope(rows, stage)
        c = Counter(r[stage] for r in pool)
        L.append(
            f"| {stage} | {scope} {len(pool)}개 | {c[DONE]} | {c[WIP]} | {c[DUE]} | {c[LATER]} |"
        )
    L.append("")

    if warnings:
        L += ["## 확인이 필요한 곳", ""] + [f"- {w}" for w in warnings] + [""]

    parts: "OrderedDict[int, list[dict]]" = OrderedDict()
    for r in rows:
        parts.setdefault(r["파트번호"], []).append(r)
    for no, rs in parts.items():
        L += [f"## Part {no}. {rs[0]['파트제목']}", "", f"납품: {str(rs[0]['차수']) + '차' if rs[0]['차수'] else '미배정'}", ""]
        chapter = None
        for r in rs:
            if r["챕터"] != chapter:
                chapter = r["챕터"]
                if chapter:
                    L += [f"### {chapter}", ""]
                L += [
                    "| 클립 | 제목 | 길이 | 장수 | 제작 | 대본 | 촬영 | 비고 |",
                    "|---|---|---|---|---|---|---|---|",
                ]
            L.append(
                "| "
                + " | ".join(
                    [
                        r["클립"], r["제목"], r["길이"], r["장수"],
                        ("슬라이드 " if r["슬라이드"] else "실습자료 ") + r["제작"], r["대본"], r["촬영"], r["비고"] or "",
                    ]
                )
                + " |"
            )
        L.append("")
    return "\n".join(L)


def die(message: str) -> None:
    print(f"대시보드 생성 실패 — {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    quiet = "--quiet" in sys.argv
    rows, warnings, nearest = build_rows()
    try:
        manifest = json.loads(read(ROOT / "dashboard" / "clips.json") or "{}")
    except json.JSONDecodeError:
        manifest = {}
    _, schedule, _ = delivery_config(manifest)

    targets = {
        ROOT / "dashboard" / "index.html": render_html(rows, warnings, nearest, schedule),
        ROOT
        / "docs"
        / "production-status.md": render_markdown(rows, warnings, nearest) + "\n",
    }
    changed = []
    for path, content in targets.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if read(path) != content:
            path.write_text(content, encoding="utf-8")
            changed.append(path.relative_to(ROOT))

    if not quiet or changed or warnings:
        summary = []
        for stage, _, _ in STAGES:
            pool = stage_scope(rows, stage)
            summary.append(
                f"{stage} {Counter(r[stage] for r in pool)[DONE]}/{len(pool)}"
            )
        print(f"대시보드 {len(rows)}클립 — " + " · ".join(summary))
        for path in changed:
            print(f"  갱신 {path}")
        if not changed:
            print("  변경 없음")
        for w in warnings:
            print(f"  ⚠ {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
