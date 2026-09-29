# 영업팀 구조 살펴보기 (교차 검증) 스토리보드

**소스:** `../_source/ch01-02-sales-team-structure.md`
**출력 슬라이드:** `artifacts/part6/outputs/ch01-02-sales-team-structure.html`
**총 슬라이드:** 9장 (표지 1장 + 본문 8장)
**디자인 기준:** fastcampus-slide `assets/base-template.html` (패턴 30~34는 무료 세미나 참고 덱 이식)

## 슬라이드 구성

| # | 타입 | 제목 | 화면 |
|---|---|---|---|
| 1 | COVER_SCENE | 영업팀 구조 살펴보기 | 광고주 → 대행사 담당자 → 작성·검사 로봇으로 이어지는 생성 이미지 1점 |
| 2 | PROCESS_STRIP | 누가 누구에게 내는가 | 무브펫(광고주) → 포커스온(대행사) → 제안서·견적서 |
| 3 | SEMINAR_ROLE_MAP_PARALLEL | 영업팀의 구조 | 사람 → Coordinator → 작성자(Codex)·평가자(Claude Code) 배정 지도 |
| 4 | SEMINAR_IO_FLOW | 작성자가 읽는 것 | 브리프·회사 문서·양식 → 작성자 → 요구사항 정의서와 초안 |
| 5 | SEMINAR_IO_FLOW | 평가자가 보는 것 | 초안·체크리스트·요구사항 → 평가자 → 평가 기록 |
| 6 | SCENE_COMPARE | 숫자는 다시 계산한다 | 읽어서 판단할 것(purple) + 계산해서 확인할 것(yellow) |
| 7 | REVIEW_LOOP | 한 라운드의 모양 | 초안 → 평가·검산 → 판정, 아래 반려 점선 |
| 8 | SCENE_COMPARE | 남는 기록 | 최종 제안서와 교차 검토 보고서 실제 캡처 두 장 |
| 9 | SCENE_PAIR | 루프는 한 번에 돈다 | 선언문과 세 줄 정리 |

## 사실 규율

무브펫은 광고주, 포커스온은 광고대행사다. 회사 문서는 Part 4에서 만든 본인 회사 문서로 대체할 수 있다. 검산 스크립트는 값을 코드에 넣지 않고 실행할 때마다 입력받는다. 캡처의 항목 수·라운드 수를 목표로 제시하지 않는다.

## 이미지

`_images/ch01-02--sales-team-transparent.png` (표지, codex 생성) · `ch01-02--proposal-quote-final.png`·`ch01-02--cross-review-report.png` (8장, 실제 결과 캡처).