# 확정 덱 경계 애니메이션 점검 — 2026-09-09

사용자 요청: 촬영 완료를 제외한 확정 덱에서 포함 구조의 경계 등장 누락을 고치고, 중립 템플릿에 같은 규격을 추가한다.

## 범위

- 최신 인덱스의 확정 HTML 8개 덱, 53장. Part 4 두 클립은 사용자 최종 확정 및 인덱스 상태를 적용했다. 오래된 confirmed-decks.json의 누락을 미확정으로 해석하지 않았다.
- 촬영 상태 기준: dashboard/clips.json. ch02-01-setup-prep, ch02-03-screen-and-board는 촬영 완료이므로 수정하지 않음.
- 외부 Google Slides 두 항목은 로컬 HTML·템플릿 점검 대상에 포함하지 않음.
- repo-and-flow 4·5번의 data-motion="none", 브랜치·워크트리 덱의 클릭 전환 유지.

## 결과

| 덱 | 장수 | 결과 |
|---|---:|---|
| ch02-01-single-agent-limits | 5 | 동일 유형 누락 없음 · 파일 유지 |
| ch01-01-terminal-problem | 5 | 동일 유형 누락 없음 · 파일 유지 |
| ch01-02-what-is-orca | 5 | 2번 경계 애니메이션 보정 |
| ch01-01-what-is-git | 5 | 동일 유형 누락 없음 · 파일 유지 |
| ch01-02-repo-and-flow | 8 | 동일 유형 누락 없음 · 파일 유지 |
| ch01-03-branch-vs-worktree | 8 | 7번 경계 애니메이션 보정 |
| ch01-01-orchestration-structure | 8 | 3번 경계 애니메이션 보정 |
| ch01-02-goal-task-flow | 9 | 3번 경계 애니메이션 보정 |

## 구현과 검수

- 컨테이너 테두리의 자리와 두께를 유지하고, 같은 외곽에 scope-frame을 배치해 경계만 opacity로 등장시킨다. 내부 요소의 순차 등장을 부모의 opacity·transform으로 묶지 않는다.
- 0ms에서 경계 숨김, 400ms에서 경계 등장 및 후속 요소 대기, 완료 시 전체 표시 확인. 선은 opacity와 함께 clip-path도 확인했다.
- 재진입 시 0ms로 초기화, reduced-motion에서는 모든 요소를 지연 없이 표시.
- 804×512·1280×800·2133×1200에서 프레임 경계와 컨테이너 위치 일치, 이미지 로딩·넘침·브라우저 오류 확인.
- 수정 전 파일 해시와 대조해 실제 변경된 출력 HTML이 위 4개 파일뿐임을 확인. 대본·슬라이드 문구·장수는 유지.
- 상세 결과: boundary-animation-verification.json. 점검 전 상태: boundary-animation-audit-before.json.

## 템플릿

- .claude/skills/fastcampus-slide/assets/base-template.html의 9번 CONTAINED_STRUCTURE 추가. 상위 범위·공통 목적·항목 A/B/C·공유 정보의 중립 슬롯으로 구성.
- data-anim-step 실행 순서와 경계 전용 scope-frame 규격, 재진입과 모션 감소 대응 포함. 템플릿도 위 단계·크기 검수를 통과.
- SKILL.md, references/slide-layouts.md, CLAUDE.md의 패턴 수·선택 기준·초기/중간 프레임 검수 항목 동기화. .agents 심링크 유지.
