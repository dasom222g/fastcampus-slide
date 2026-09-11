# 승인 패턴 라이브러리 검수 — 2026-09-11

- 기존 9종 + 승인 덱에서 추출한 20종 = **29종**. 새 유형의 원본·사용 조건·적용 한계는 `goldenset-manifest.json`과 스킬의 `pattern-catalog.md`에 기록.
- 승인 HTML 8개, 54장 캡처. 캡처 경로는 manifest의 `screenshots`. 원본 HTML의 SHA-256은 추출 전후 동일.
- 템플릿 29종 × 1280×800 / 2133×1200 / 804×512 = 87개 조합. 최종 본문 넘침 0, 깨진 이미지 0. `template-validation.json` 참고.
- 클릭 상호작용 12개 검사 통과. 자동 실행 없음, 클릭 fade, 즉시 이동, 재생, 재진입, 키보드 작동, 클릭으로 덱이 넘어가지 않음.
- 모션 감소: 클릭 전 위치 820, 클릭 후 최종 위치 530, 이동 애니메이션 없음. `interaction-validation.json` 참고.
- 템플릿 JavaScript 구문 검사, 스킬 quick_validate, 로컬 문서 링크, git diff --check 통과.
- 새 읽기 전용 검수 코드 `inspect-slide-layout.js`를 실제 브라우저에서 실행해 확인.
- `.claude` 원본과 `.agents` 심링크 유지. 촬영 상태·승인 덱·대본·커리큘럼은 이 작업에서 변경하지 않음.

전체 캡처만으로 인과관계가 검증되지는 않는다. 의미의 판단은 골든셋의 실패→수정 사례와 승인 원본을 함께 따른다.
