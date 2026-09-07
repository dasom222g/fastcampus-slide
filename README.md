# FastCampus Slides — Orca 강의

패스트캠퍼스 **Orca 강의**(나 대신 일하는 AI 팀 만들기)의 이론 슬라이드 저장소입니다.
전체 10개 파트 · 72클립 중 슬라이드가 있는 클립만 덱으로 만듭니다.

## 문서 세 개가 각각 다른 것을 정합니다

| 문서 | 무엇을 정하는가 |
|---|---|
| `docs/curriculum.md` | 파트·챕터·클립의 번호·제목·길이 → **파일 이름의 기준** |
| `docs/course-brief.md` | 청중·톤·용어 규칙·강의를 관통하는 축 → **어떻게 말할지의 기준** |
| `artifacts/<part>/_source/<clip>.md` | 클립별 슬라이드 구성안(소스) → **무엇을 몇 장에 담을지의 기준** |

## 구조

폴더는 **파트 단위**로만 나눕니다. 종류 구분은 파트 폴더 안에서 `_` 폴더로 합니다.

```
artifacts/
  part2/
    ch02-01-setup-prep.html        ← 배포되는 덱. 공개 주소 /part2/ch02-01-setup-prep
    _source/ch02-01-setup-prep.md  이 클립의 슬라이드 소스 (구성안·참고 자료)
    _storyboard/ch02-01-setup-prep.md
    _feedback/ch02-01-setup-prep.md
    _images/ch02-01-setup-prep/
assets/                            모든 덱이 공유하는 로고
index.html                         덱 목록 (커리큘럼 순서)
```

**덱과 부속 문서는 확장자만 빼고 이름이 같습니다.** 파일명은 커리큘럼의 클립 번호를 그대로 씁니다 — `Ch02-01` → `ch02-01-<영문슬러그>`.

`vercel.json`의 rewrite가 `/<part>/<clip>` → `/artifacts/<part>/<clip>.html`로 연결합니다.
HTML 안의 에셋 경로는 **루트 절대경로**(`/assets/...`)만 씁니다.
`_`로 시작하는 폴더와 `docs/`는 `.vercelignore`로 배포에서 제외됩니다.

## 새 슬라이드 만들기

`.claude/skills/fastcampus-slide` 스킬이 소스 분석 → 스토리보드 → HTML → 피드백 파일까지 처리합니다.
Claude Code에서 클립을 지목하면 됩니다 — 예: `Part 1 Ch01-01 슬라이드 만들어줘`

## 로컬 미리보기

루트 절대경로와 rewrite 때문에 `file://`로 열면 에셋이 깨집니다.

```bash
vercel dev    # http://localhost:3000/part2/ch02-01-setup-prep
```
