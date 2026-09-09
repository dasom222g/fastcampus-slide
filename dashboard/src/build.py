#!/usr/bin/env python3
"""저장소를 스캔해 슬라이드 제작 현황을 다시 만든다.

만드는 것
  dashboard/index.html          보기용 대시보드
  docs/production-status.md     같은 표의 마크다운본 (커밋 diff로 변화를 읽는다)

읽는 것
  docs/curriculum.md            파트·챕터·클립의 번호·제목·길이 — 여기가 유일한 출처
  dashboard/clips.json          슬라이드를 만들 클립 목록 + 촬영 상태(수기) + 예외
  artifacts/<part>/outputs/     덱 HTML 존재 여부와 실제 장수
  artifacts/<part>/_source/     소스 frontmatter의 슬라이드 장수·상태
  artifacts/<part>/_script/     대본 존재 여부와 대본이 적은 장수
  artifacts/CONFIRMED.md        확정 여부

판정 규칙
  제작  HTML 없음 → 시작전 / 있고 확정 → 완료 / 있고 확정 아님 → 작업중
  대본  _script 파일 없음 → 시작전 / 있음 → 완료
  촬영  clips.json에 적힌 값 그대로 (자동 판정 불가)
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

DONE, WIP, TODO = "완료", "작업중", "시작전"
STATES = (DONE, WIP, TODO)
CLS = {DONE: "done", WIP: "wip", TODO: "todo"}
GLYPH = {DONE: "●", WIP: "◐", TODO: "○"}

STAGES = (
    ("제작", "HTML 덱이 완성됐는가"),
    ("대본", "화면과 일치하는 전체 대본이 있는가"),
    ("촬영", "영상 수록을 마쳤는가"),
)


# ── 읽기 ────────────────────────────────────────────────────────────


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_curriculum() -> dict[tuple[int, str], dict]:
    """`- Ch01-01. 제목 (11분)` 줄을 파트·챕터와 함께 읽는다."""
    text = read(ROOT / "docs" / "curriculum.md")
    if not text:
        die("docs/curriculum.md 를 찾을 수 없다.")

    clips: dict[tuple[int, str], dict] = {}
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
                "챕터": chapter,
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


# ── 판정 ────────────────────────────────────────────────────────────


def build_rows() -> tuple[list[dict], list[str], int]:
    curriculum = parse_curriculum()
    manifest_path = ROOT / "dashboard" / "clips.json"
    try:
        manifest = json.loads(read(manifest_path) or "{}")
    except json.JSONDecodeError as exc:
        die(f"dashboard/clips.json 을 읽을 수 없다 — {exc}")

    entries = manifest.get("클립")
    if not entries:
        die("dashboard/clips.json 의 「클립」 목록이 비어 있다.")

    confirmed = read(ROOT / "artifacts" / "CONFIRMED.md")
    rows, warnings = [], []

    for e in entries:
        part, clip = e.get("파트"), e.get("클립")
        meta = curriculum.get((part, clip))
        if not meta:
            warnings.append(
                f"Part {part} {clip} — 커리큘럼에 없는 클립이다. clips.json을 확인한다."
            )
            continue

        slug = e.get("슬러그")
        row = dict(meta)
        row["슬러그"] = slug
        row["비고"] = e.get("비고", "")

        deck_text = source_text = script_text = ""
        if slug:
            deck_text = read(ROOT / "artifacts" / f"part{part}" / "outputs" / f"{slug}.html")
            source_text = read(ROOT / "artifacts" / f"part{part}" / "_source" / f"{slug}.md")
            script_text = read(ROOT / "artifacts" / f"part{part}" / "_script" / f"{slug}.md")

        fm = frontmatter(source_text)
        declared = declared_count(fm.get("슬라이드", ""))
        actual = slide_count(deck_text) if deck_text else None
        count = e.get("장수") or declared or actual
        row["장수"] = f"{count}장" if count else "—"

        # 제작
        if deck_text:
            is_confirmed = (slug in confirmed) or ("확정" in fm.get("상태", ""))
            made = DONE if is_confirmed else WIP
        else:
            made = TODO
        # 대본
        scripted = DONE if script_text.strip() else TODO

        for stage, auto in (("제작", made), ("대본", scripted)):
            if stage in e:
                value = e[stage]
                if value not in STATES:
                    die(f"Part {part} {clip} 의 「{stage}」 값이 이상하다: {value!r}")
                if value != auto:
                    reason = e.get(f"{stage}_사유", "")
                    row["비고"] = (row["비고"] + " · " if row["비고"] else "") + (
                        reason or f"{stage} 수기 지정"
                    )
                if stage == "제작":
                    made = value
                else:
                    scripted = value

        shot = e.get("촬영", TODO)
        if shot not in STATES:
            die(f"Part {part} {clip} 의 「촬영」 값이 이상하다: {shot!r}")

        row["제작"], row["대본"], row["촬영"] = made, scripted, shot

        if not row["비고"] and slug is None:
            row["비고"] = "소스 없음"

        # 어긋난 곳은 커밋 시점에 잡아준다
        label = f"Part {part} {clip}"
        if declared and actual and declared != actual:
            warnings.append(
                f"{label} — 소스는 {declared}장인데 덱은 {actual}장이다."
            )
        if script_text:
            sc = declared_count(script_text.splitlines()[0])
            ref = declared or actual
            if sc and ref and sc != ref:
                warnings.append(f"{label} — 대본은 {sc}장인데 덱은 {ref}장이다.")
        if slug and not deck_text and made != TODO and not e.get("제작_사유"):
            warnings.append(f"{label} — 덱 HTML이 없는데 제작이 {made}로 적혀 있다.")

        rows.append(row)

    return rows, warnings, len(curriculum)


# ── 그리기 ──────────────────────────────────────────────────────────


def esc(s: str) -> str:
    return html.escape(s or "")


def track_html(row: dict) -> str:
    cells = []
    for stage, _ in STAGES:
        st = row[stage]
        cells.append(
            f'<span class="stage stage--{CLS[st]}" title="{stage} {st}">'
            f'<span class="stage__dot" aria-hidden="true">{GLYPH[st]}</span>'
            f'<span class="stage__txt">{st}</span></span>'
        )
    link = '<span class="track__link" aria-hidden="true"></span>'
    return '<span class="track">' + link.join(cells) + "</span>"


def render_gates(rows: list[dict]) -> str:
    total = len(rows)
    out = []
    for i, (stage, hint) in enumerate(STAGES, start=1):
        c = Counter(r[stage] for r in rows)
        d, w = c[DONE], c[WIP]
        wip_html = f"<em>작업중 {w}</em>" if w else ""
        out.append(f"""<li class="gate">
        <span class="gate__step">{i}</span>
        <div class="gate__body">
          <h3 class="gate__name">{stage}</h3>
          <p class="gate__hint">{hint}</p>
          <div class="gate__bar" role="img" aria-label="{stage} 완료 {d}, 작업중 {w}, 시작전 {c[TODO]}, 전체 {total}">
            <span class="gate__fill gate__fill--done" style="width:{d / total * 100:.4f}%"></span>
            <span class="gate__fill gate__fill--wip" style="width:{w / total * 100:.4f}%"></span>
          </div>
          <p class="gate__nums"><b>{d}</b><span class="gate__of">/{total} 완료</span>{wip_html}</p>
        </div>
      </li>""")
    return "\n".join(out)


def render_parts(rows: list[dict]) -> str:
    parts: OrderedDict[int, list[dict]] = OrderedDict()
    for r in rows:
        parts.setdefault(r["파트번호"], []).append(r)

    out = []
    for no, rs in parts.items():
        done = sum(1 for r in rs for s, _ in STAGES if r[s] == DONE)
        total = len(rs) * len(STAGES)
        pct = done / total * 100
        title = esc(rs[0]["파트제목"])
        out.append(f"""<section class="part">
      <header class="part__head">
        <h3 class="part__name">Part {no}</h3>
        <span class="part__title">{title}</span>
        <span class="part__meter" role="img" aria-label="공정 {done}/{total} 완료">
          <span class="part__meter-fill" style="width:{pct:.4f}%"></span>
        </span>
        <span class="part__pct">{done}/{total}</span>
      </header>
      <div class="tablewrap">
      <table class="grid">
        <thead><tr>
          <th scope="col" class="c-clip">클립</th>
          <th scope="col" class="c-title">제목</th>
          <th scope="col" class="c-num">길이</th>
          <th scope="col" class="c-num">장수</th>
          <th scope="col" class="c-track">제작 → 대본 → 촬영</th>
          <th scope="col" class="c-note">비고</th>
        </tr></thead>
        <tbody>""")
        for r in rs:
            out.append(f"""<tr>
            <td class="c-clip"><code>{esc(r["클립"])}</code></td>
            <td class="c-title">{esc(r["제목"])}</td>
            <td class="c-num">{esc(r["길이"])}</td>
            <td class="c-num">{esc(r["장수"])}</td>
            <td class="c-track">{track_html(r)}</td>
            <td class="c-note">{esc(r["비고"])}</td>
          </tr>""")
        out.append("        </tbody>\n      </table>\n      </div>\n    </section>")
    return "\n".join(out)


def render_warnings(warnings: list[str]) -> str:
    if not warnings:
        return (
            '<p class="check check--ok"><b>어긋난 곳 없음.</b> '
            "소스의 장수, 덱의 실제 장수, 대본의 장수가 모두 맞는다.</p>"
        )
    items = "".join(f"<li>{esc(w)}</li>" for w in warnings)
    return (
        f'<p class="check check--warn"><b>{len(warnings)}건이 어긋난다.</b></p>'
        f'<ul class="checklist">{items}</ul>'
    )


def render_html(rows: list[dict], warnings: list[str], all_clips: int) -> str:
    template = read(SRC / "template.html")
    if not template:
        die("dashboard/src/template.html 을 찾을 수 없다.")
    counts = {
        stage: Counter(r[stage] for r in rows) for stage, _ in STAGES
    }
    return (
        template.replace("{{GATES}}", render_gates(rows))
        .replace("{{PARTS}}", render_parts(rows))
        .replace("{{WARNINGS}}", render_warnings(warnings))
        .replace("{{TOTAL}}", str(len(rows)))
        .replace("{{ALL_CLIPS}}", str(all_clips))
        .replace("{{NO_SLIDE}}", str(all_clips - len(rows)))
        .replace("{{SHOT_DONE}}", str(counts["촬영"][DONE]))
        .replace("{{BUILT}}", date.today().isoformat())
    )


def render_markdown(rows: list[dict], warnings: list[str], all_clips: int) -> str:
    L = [
        "---",
        "문서: 슬라이드 제작 현황",
        "상태: dashboard/src/build.py 가 생성한다 — 직접 고치지 않는다",
        f"최종 생성: {date.today().isoformat()}",
        "---",
        "",
        "# 슬라이드 제작 현황",
        "",
        f"커리큘럼 {all_clips}클립 중 슬라이드가 필요한 **{len(rows)}클립**을 "
        "제작 → 대본 → 촬영 순으로 추적한다.",
        "촬영만 수기이고 나머지는 저장소를 스캔해 판정한다. 고칠 곳은 `dashboard/clips.json`이다.",
        "",
        "| 공정 | 완료 | 작업중 | 시작전 |",
        "|---|---:|---:|---:|",
    ]
    for stage, _ in STAGES:
        c = Counter(r[stage] for r in rows)
        L.append(f"| {stage} | {c[DONE]} | {c[WIP]} | {c[TODO]} |")
    L.append("")

    if warnings:
        L.append("## 어긋난 곳")
        L.append("")
        L += [f"- {w}" for w in warnings]
        L.append("")

    parts: OrderedDict[int, list[dict]] = OrderedDict()
    for r in rows:
        parts.setdefault(r["파트번호"], []).append(r)
    for no, rs in parts.items():
        L.append(f"## Part {no}. {rs[0]['파트제목']}")
        L.append("")
        L.append("| 클립 | 제목 | 길이 | 장수 | 제작 | 대본 | 촬영 | 비고 |")
        L.append("|---|---|---|---|---|---|---|---|")
        for r in rs:
            L.append(
                "| "
                + " | ".join(
                    [
                        r["클립"], r["제목"], r["길이"], r["장수"],
                        r["제작"], r["대본"], r["촬영"], r["비고"] or "",
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
    rows, warnings, all_clips = build_rows()

    targets = {
        ROOT / "dashboard" / "index.html": render_html(rows, warnings, all_clips),
        ROOT / "docs" / "production-status.md": render_markdown(rows, warnings, all_clips) + "\n",
    }
    changed = []
    for path, content in targets.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if read(path) != content:
            path.write_text(content, encoding="utf-8")
            changed.append(path.relative_to(ROOT))

    if not quiet or changed or warnings:
        counts = " · ".join(
            f"{s} {Counter(r[s] for r in rows)[DONE]}/{len(rows)}" for s, _ in STAGES
        )
        print(f"대시보드 {len(rows)}클립 — {counts}")
        for path in changed:
            print(f"  갱신 {path}")
        if not changed:
            print("  변경 없음")
        for w in warnings:
            print(f"  ⚠ {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
