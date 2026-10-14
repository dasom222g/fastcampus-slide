# 3차 납기분 HTML 제작 검수

- 제작일: 2026-10-09
- 범위: Part 8~10의 이론 클립 7개, 총 46장.
- 2026-10-12 사용자 정정: Part 8 Ch02-01 회차 소재 선정 기준은 실습 클립이다. 사용자 요청으로 그 덱의 3장 「소재 선정 기준」만 Ch01-01 5장으로 옮기고(Ch01-01 8장), Ch02-01 HTML·소스·스토리보드·피드백·검수 캡처는 삭제했다. 유효한 덱은 6개 41장이다. 아래 표와 `batch3-validation.json`·`batch3-navigation.json`의 Ch02-01 기록은 당시 이력이다.
- 2026-10-12 사용자 정정: Part 8~10 본문 장의 제목 전체가 키컬러였다. 이전 파트처럼 강조 단어에만 `.hl`을 씌우고 스토리보드에 `제목 강조(.hl)`를 기록했다. 「세 축」「세 가지」 같은 표현을 빼고 「플랫폼별」 등으로 바꿨다(커리큘럼 클립명 「한 명이 세 플랫폼을…」은 유지).
- 상태: 사용자 검수 전. 확정 목록·촬영 상태는 변경하지 않았다.
- 전용 소스가 없어 기존 커리큘럼·강의 기획서·실습자료·공식 자료로 소스를 작성하고 스토리보드를 먼저 저장했다.

| 파트 | 클립 | 장수 | HTML |
|---|---|---:|---|
| 8 | 콘텐츠팀 구조 살펴보기 (R&R 분배) | 7 | `artifacts/part8/outputs/ch01-01-content-team-rr.html` |
| 8 | 회차 소재 선정 기준 | 6 | `artifacts/part8/outputs/ch02-01-topic-selection.html` |
| 8 | 한 명이 세 플랫폼을 다 쓰면 생기는 일 | 6 | `artifacts/part8/outputs/ch03-01-platform-role-separation.html` |
| 9 | 모바일의 역할 | 6 | `artifacts/part9/outputs/ch01-01-mobile-role.html` |
| 10 | 팀을 굴리면 토큰이 몇 배로 드는가 | 7 | `artifacts/part10/outputs/ch01-01-multi-agent-token-cost.html` |
| 10 | 모델 분리 설계 전략 | 7 | `artifacts/part10/outputs/ch02-01-model-allocation.html` |
| 10 | 강의 정리 | 7 | `artifacts/part10/outputs/ch03-01-course-wrap-up.html` |

## 검수

- 1920×1080과 1280×800 CSS px, 확대율 100%에서 전체 92개 화면 상태 확인.
- 각 덱의 data-index를 기록하여 전 장이 누락 없이 검수되었음을 확인.
- 본문 경계 넘침·헤더 넘침·깨진 이미지·로고 누락 0건.
- 실제 렌더 캡처는 각 파트 `_qa/`에 보관. 최종 배치를 육안 확인.
- 정상 모션 1차 검수 및 최종 모션 감소 설정 검수.
- HTML·소스·스토리보드·피드백 장수 일치, 표지 제목은 커리큘럼과 일치.
- 소요시간·템플릿 자리표시자·이동용 좌우 버튼 없음.
- 대시보드 기존 테스트 19개 통과, git diff --check 통과.
- 상세 결과: `batch3-validation.json`, `batch3-navigation.json`.

## 내용 근거

- 콘텐츠팀: 최신 실습 가이드와 recipe-content-boilerplate의 채널 소개·문서 저장 규칙.
- 소재 이미지: 기존 project4-recipe-content의 케이크 이미지 재사용.
- 모바일: https://www.onorca.dev/ 의 모바일 동반 앱·데스크톱 페어링·터미널 설명.
- 토큰: https://www.anthropic.com/engineering/multi-agent-research-system 의 채팅 대비 약 4×·15× 사례. 고정 배수·요금 배수로 설명하지 않았다.
- 요금 구조: https://platform.claude.com/docs/en/about-claude/pricing . 모델별 구체 가격은 수록하지 않았다.
- 모델 배정 기준은 강의용 적용으로 표시하고, 고정 모델 순위로 단정하지 않았다.

## 대본

HTML 덱 전체의 사용자 최종 승인 후 작성한다. 이번 작업에서 대본을 생성하지 않았다.
