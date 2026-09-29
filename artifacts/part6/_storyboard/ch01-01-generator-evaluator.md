# Generator–Evaluator 패턴이란 스토리보드

**소스:** `../_source/ch01-01-generator-evaluator.md`
**출력 슬라이드:** `artifacts/part6/outputs/ch01-01-generator-evaluator.html`
**총 슬라이드:** 9장 (표지 1장 + 본문 8장)
**디자인 기준:** fastcampus-slide `assets/base-template.html` (패턴 30~34는 무료 세미나 참고 덱 이식)

## 슬라이드 구성

| # | 타입 | 제목 | 화면 |
|---|---|---|---|
| 1 | COVER_SCENE | Generator–Evaluator 패턴이란 | 작성 로봇과 검사 로봇을 나눈 생성 이미지 1점 |
| 2 | SCENE_COMPARE | 자기 결과는 자기가 통과시킨다 | 같은 에이전트에게 다시 묻기(orange) ≠ 판정하는 쪽을 따로 두기(purple) |
| 3 | STRUCTURE_EXCHANGE | 만드는 쪽과 판정하는 쪽 | Generator(brand)·Evaluator(purple) 두 패널과 초안·반려 양방향 화살표 |
| 4 | OPEN_TRIPTYCH | 다른 모델로 평가하는 이유 | 같은 판단 습관 · 다른 하네스 · 보장은 아니다 3열 |
| 5 | PROCESS_STRIP | 기준은 먼저, 따로 | 기준 작성 → 매 라운드 동일 적용 → 작성자에게 비공개 |
| 6 | GOAL_ACCEPTANCE | 판정은 항목별로 | 체크리스트 4항목의 Y/N과 반려 판정 |
| 7 | SEMINAR_IO_FLOW | 반려는 사유와 함께 | 평가 기록의 N 항목·고칠 내용 → 평가자 → 수정 요청서 |
| 8 | REVIEW_LOOP | 통과할 때까지 도는 루프 | 초안 → 평가·검산 → 통과, 아래 반려 점선과 다음 라운드 연결 |
| 9 | SCENE_PAIR | 어디에 쓰나 | 선언문과 세 줄 정리 |

## 앞 파트와 겹치지 않게

Part 5 Ch01-02에서 **검증 오류**를 실패 셋 중 하나로 다뤘다. 이 덱은 그 해결을 펼치는 자리이므로, 문제 설명은 2장 하단 한 줄 회수로만 처리하고(“Part 5에서 본 검증 오류가 이 자리입니다”) 기준·판정·반려·라운드로 바로 들어간다.

## 사실 규율

다른 모델을 쓰면 오류가 사라진다고 말하지 않는다. 체크리스트 항목 수와 반려 횟수는 실행마다 다르므로 특정 숫자를 목표로 제시하지 않는다.

## 색

작성 brand · 평가 purple · 기준·대기 yellow · 통과 green · 반려 orange · 사람 gray.
