# edu-note 바인딩 (패스트캠퍼스 Orca 강의)

`edu-note` 스킬이 작업 전에 읽는 파일이다. 스킬 원본은 이 저장소가 아니라
**common-skills**(`~/somi/github.com/dasom222g/common-skills/skills/edu-note`)에 있고,
전역 심링크로 Claude·Codex 양쪽에서 보인다. 스킬은 문서 규격(구조·문체·밀도)만 정하고,
아래 맥락·경로·독자는 이 저장소가 정한다.

## 맥락 문서

작업 전에 읽는다. 어긋나면 아래 순서로 이긴다.

- `docs/confirmed-copy.md` — **강사가 확정한 문구.** 용어·정의·프로젝트 명칭이 여기서 온다. 다른 문서와 어긋나면 이것이 이긴다
- `docs/curriculum.md` — 파트·챕터·클립의 번호·제목·길이. **파일 이름의 기준**
- `docs/course-brief.md` — 청중·톤·용어 규칙·강조점. **어떻게 말할지의 기준**
- `docs/patterns.md` — 멀티에이전트 패턴 4가지. 패턴이 등장하는 클립이면 반드시 읽는다
- `artifacts/<part>/_source/<clip>.md` — 그 클립에서 무엇을 다뤘는지 (슬라이드 소스)
- `artifacts/<part>/_script/<clip>.md` — 그 클립에서 실제로 말한 것 (발표 대본)

랩노트는 **슬라이드에서 설명한 것을 수강생이 자기 손으로 재현하게 만드는 문서**다.
슬라이드·대본에 없는 내용을 새로 가르치지 않고, 반대로 실행에 필요한 값을 생략하지도 않는다.

## 경로

| 역할 | 경로 |
|---|---|
| 입력 (원자료) | `artifacts/<part>/_edu-note/_source/<clip>.md` |
| 출력 (완성 문서) | `artifacts/<part>/_edu-note/<clip>.md` |
| 피드백 | `artifacts/<part>/_edu-note/_feedback/<clip>.md` |

파일명 규칙: 덱·대본과 **같은 클립 슬러그**를 쓴다 (`ch02-01-single-agent-limits`처럼
`<ch>-<n>-<slug>`). 커리큘럼의 번호·제목이 기준이다.

만드는 단위도 덱과 같다 — **클립 하나에 랩노트 하나**. 사용자가 지목하지 않은 클립을 먼저 만들지 않는다.

## 독자

패스트캠퍼스 수강생. 해당 클립 영상을 이미 봤고, 화면을 옆에 켜두고 그대로 따라 하려는 사람이다.
강의 기획서(`docs/course-brief.md`)의 청중 정의를 따르며, 거기서 "이미 안다"고 전제한 것은 다시 설명하지 않는다.

## 저장된 제작 원자료

- [Part 3 Ch02-02 — GitHub 가입 및 Orca에 연결하기](../artifacts/part3/_edu-note/_source/ch02-02-github-orca-connect.md): 첫 실습의 수동·자동 범위와 단계별 이해 목표. 실제 실습 로그가 아닌 제작 기획 원자료이며, 실습자료 제작 시 먼저 참고한다.
