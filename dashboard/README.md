# 제작 현황 대시보드

슬라이드가 필요한 클립이 **제작 → 대본 → 촬영** 중 어디까지 갔는지 한 화면에 모은다.
**커밋할 때마다 자동으로 다시 만들어진다.**

## 켜기

저장소를 새로 클론했을 때 한 번만 실행한다.

```bash
sh dashboard/install.sh
```

`git config core.hooksPath dashboard/hooks`를 걸어 훅을 켠다. 끄려면 `git config --unset core.hooksPath`.

## 무엇이 자동이고 무엇이 수기인가

| 공정 | 어떻게 정해지나 |
|---|---|
| **제작** | 자동 — 덱 HTML이 없으면 `시작전`, 있으면 `작업중`, `CONFIRMED.md`에 있거나 소스 `상태`에 확정이 있으면 `완료` |
| **대본** | 자동 — `artifacts/<part>/_script/<clip>.md`가 있으면 `완료` |
| **촬영** | **수기** — 저장소에 촬영 기록이 없다. `clips.json`에서 직접 적는다 |

번호·제목·길이는 `docs/curriculum.md`가 정한다. 여기에 옮겨 적지 않는다.

## 촬영을 끝냈을 때

`dashboard/clips.json`에서 해당 클립의 `촬영`을 `완료`로 바꾸고 커밋하면 끝이다.

```json
{ "파트": 3, "클립": "Ch01-01", "슬러그": "ch01-01-what-is-git", "촬영": "완료" }
```

## 새 클립에 슬라이드를 만들기로 했을 때

`clips.json`의 `클립` 배열에 한 줄 더한다. `슬러그`는 소스를 만들기 전이면 `null`로 둔다.

```json
{ "파트": 5, "클립": "Ch02-02", "슬러그": null, "촬영": "시작전" }
```

## 자동 판정이 틀렸을 때

`제작` 또는 `대본` 키를 직접 적으면 그 값이 이긴다. 왜 덮어썼는지 `_사유`에 남긴다 —
남기지 않으면 「맞물림 검사」가 어긋난 것으로 잡는다.

```json
{
  "파트": 1, "클립": "Ch01-01", "슬러그": "ch01-01-course-intro",
  "촬영": "시작전",
  "제작": "완료",
  "제작_사유": "Google Slides로 제작·확정. 저장소에 HTML 덱이 없다"
}
```

## 맞물림 검사

빌드할 때마다 아래를 확인하고 대시보드 「맞물림 검사」와 커밋 로그에 띄운다.

- 소스 frontmatter의 `슬라이드: N장` ↔ 덱 HTML의 실제 장수
- 대본 첫 줄의 `(N장)` ↔ 덱의 장수
- `제작`이 완료·작업중인데 덱 HTML이 없는 경우
- `clips.json`에 있는데 커리큘럼에 없는 클립

## 만들어지는 것

| 파일 | 무엇 |
|---|---|
| `dashboard/index.html` | 보기용 대시보드. 배포되면 `/dashboard` |
| `docs/production-status.md` | 같은 표의 마크다운본. 커밋 diff로 무엇이 진행됐는지 읽는다 |

둘 다 생성물이다. **직접 고치지 않는다** — 다음 커밋에서 덮어쓴다.

## 구조

```
dashboard/
  clips.json        수기 데이터 — 클립 목록 · 촬영 · 예외
  index.html        생성물
  install.sh        훅 켜기
  hooks/pre-commit  커밋 트리거
  src/build.py      스캔하고 그린다
  src/template.html 화면 껍데기
```

## 손으로 돌리기

```bash
python3 dashboard/src/build.py
```
