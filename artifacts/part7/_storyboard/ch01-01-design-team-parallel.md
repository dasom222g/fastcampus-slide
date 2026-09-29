# 디자인팀 구조 살펴보기 (병렬 실행) 스토리보드

**소스:** `../_source/ch01-01-design-team-parallel.md`
**출력 슬라이드:** `artifacts/part7/outputs/ch01-01-design-team-parallel.html`
**총 슬라이드:** 9장 (표지 1장 + 본문 8장)
**디자인 기준:** fastcampus-slide `assets/base-template.html` (패턴 30~34는 무료 세미나 참고 덱 이식)

## 슬라이드 구성

| # | 타입 | 제목 | 화면 |
|---|---|---|---|
| 1 | COVER_SCENE | 디자인팀 구조 살펴보기 | 사람이 의뢰서를 들고, 좌우 분리된 두 책상에서 에이전트가 각자 화면을 만드는 생성 이미지 1점 |
| 2 | SCENE_COMPARE | 한 폴더에서 동시에 | 워커 A·B가 같은 `index.html`로 화살표를 보내고 폴더 위에 충돌 표시 |
| 3 | STRUCTURE_BRANCH | 작업 공간을 나눈다 | 시작 커밋 하나 → 워크트리 A(Claude Code)·B(Codex)로 갈라지는 분기 |
| 4 | SEMINAR_ROLE_MAP_PARALLEL | 디자인팀의 구조 | 사람 → Coordinator → 워커 A·B 배정 지도. 워커 라벨에 하네스와 워크트리 |
| 5 | TRANSITION_COMPARE | 같아야 하는 것과 달라도 되는 것 | 고정(brand)/열어 둠(yellow) 두 패널 |
| 6 | SEMINAR_DEPENDENCY_COMPARE | 병렬 실행이란 | 순차(앞 결과가 다음 입력)와 병렬(같은 의뢰에서 갈라짐)을 같은 시각 구조로 대비 |
| 7 | PROCESS_STRIP | 사람이 고른다 | 두 시안 → 비교 → 선택 3단. 선택은 gray(사람) |
| 8 | STRUCTURE_EXCHANGE | 선택한 시안만 메인으로 | 시안 A 선택 / 시안 B 브랜치 잔류 → 메인 머지 |
| 9 | SCENE_IMAGE | 만들 것 | 실제 완성 시안 캡처와 선언문 |

## 앞 파트와 겹치지 않게

**Part 3 Ch01-03에서 브랜치·워크트리의 정의와 관계, Orca의 작업 단위까지 다뤘다.** 이 덱은 개념을 다시 가르치지 않고 **쓰임**만 다룬다.
- 2장 하단 한 줄로만 회수한다 — "워크트리가 무엇인지는 Part 3에서 봤습니다. 이번에는 그것을 실제로 씁니다."
- 커밋·이력·분기 그림을 다시 그리지 않는다. 3장의 분기는 "같은 시작점에서 폴더 둘"이라는 배치 설명이지 이력 설명이 아니다.

## 색

사람 gray · 조율 yellow · Claude Code 축 brand · Codex 축 purple · 통과·메인 green · 충돌·문제 orange. `docs/patterns.md`의 병렬 실행 색(yellow)은 6장 패턴 대비에서만 쓴다.

## 이미지

`_images/ch01-01--parallel-desks-transparent.png` (표지, codex 생성) · `_images/ch02-01--draft-claude.png` (9장, 실제 완성 시안 캡처).