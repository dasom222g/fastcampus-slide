---
파트: part4 — 오케스트레이션과 스킬
챕터: Chapter 3. 스킬 알아보기
클립: Ch03-02. 1인 회사 운영에 유용한 스킬 모음
길이: 10분
슬라이드: 2장
산출물: artifacts/part4/outputs/ch03-02-solo-business-skills.html
상태: 확정
---

# 1인 회사 운영에 유용한 스킬 모음

Part 4 · Chapter 3 · Ch03-02 · 이론 · 2장

2026-09-19 강사 지시: 슬라이드는 표지와 ‘나만의 스킬 만들기’ 2장만 둔다. 아래 스킬별 내용은 참고 자료로 남기며 슬라이드로 만들지 않는다. ‘내 업무용 스킬’이라는 표현은 ‘나만의 스킬’로 바꾼다.

## voice-builder · social-media-skills

[GitHub · charlie947/social-media-skills](https://github.com/charlie947/social-media-skills)

README와 skills/voice-builder/SKILL.md, skills/post-writer/SKILL.md, skills/reels-scripting/SKILL.md를 확인했다. voice-builder는 인터뷰 뒤 3~5개의 글을 분석한다. 기본 결과는 프로젝트 루트의 about-me.md·voice.md다. 강의에서는 사업 정보를 더해 회사 소개서·말투 규칙으로 사용한다. 회사 사규는 사람이 직접 정한다.

social-media-skills는 스킬 모음이며 voice-builder를 포함한다. post-writer는 LinkedIn 게시글, reels-scripting은 릴스 대본용이다. 임의의 모든 플랫폼을 하나의 스킬이 자동 지원한다고 설명하지 않는다.

## grill-me

[GitHub · mattpocock/skills](https://github.com/mattpocock/skills)

skills/productivity/grill-me/SKILL.md는 grilling을 호출한다. skills/productivity/grilling/SKILL.md의 현재 방식은 지금 답할 수 있는 질문들을 라운드로 묻고 답변을 기다리는 방식이다. 무조건 한 번에 질문 하나라고 설명하지 않는다. 강의에서는 판매 아이템의 빠진 조건을 찾아내는 데 활용한다.

## marketing-skills

[GitHub · coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)

사용자 설명인 광고·랜딩·이메일 기능과 일치하는 Corey Haines의 모음을 선택했다. README와 copywriting·ad-creative·emails의 SKILL.md를 확인했다. 실제 호출은 개별 스킬로 한다. 모음 이름이 곧 단일 스킬 이름이라고 설명하지 않는다.

## Ponytail

[GitHub · DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

README와 skills/ponytail/SKILL.md를 확인했다. 기존 코드·표준 라이브러리·플랫폼 기능을 먼저 사용해 불필요한 코드를 줄인다. 일반 글 요약 도구가 아니다. 디자인 작업에서 제외하는 것은 강의의 적용 방침이며 제작자의 기능 제한으로 표현하지 않는다. 토큰 절감률을 보장하지 않는다. 적용 후 대화 내 지속 규칙과 stop ponytail 해제 안내가 있다.

## 강의 배치

- Part 4: company-identity로 회사를 인터뷰해 회사 방향성·업무 사규·프로젝트 작업 지침 3종 작성. voice-builder는 이후 콘텐츠 말투 정리에 사용.
- Part 5: grill-me로 판매 아이템을 기획하기 전 조건 구체화.
- Part 6: 추가 스킬 없이 Generator·Evaluator에 다른 모델 배정.
- Part 7: 추가 스킬 없이 Orca 디자인 모드·브라우저 개발자도구 사용.
- Part 8: marketing-skills·social-media-skills의 작업별 스킬 사용.
- Part 10: Ponytail로 구현 범위를 줄이는 방법과 토큰 사용 관찰.

## 제작 범위

2026-09-18 제작자 문서 확인. 5개 항목은 스킬과 스킬 모음을 함께 센 강의 분류다. 모두 전역 설치한다는 것은 강의 방침이다. 스킬 구매 비용과 외부 모델·도구 비용은 구분한다. 실제 설치·실습은 진행하지 않았다.

## skill-creator · 소개와 추천

[GitHub · anthropics/skills · skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

2026-09-18 제작자의 SKILL.md를 확인했다. 작업 목적·방식·원하는 출력 형식과 예시를 바탕으로 새 스킬을 작성하고, 사용 결과와 피드백으로 개선하는 도구다. 별도 모델이 아니라 에이전트가 사용하는 제작용 스킬이다. 핵심 지침 파일은 SKILL.md이며 필요한 자료를 함께 둘 수 있다. [Agent Skills 형식](https://agentskills.io/specification)도 확인했다.

배치 근거: 이 저장소 docs/curriculum.md의 Part 4 Ch03-02에 ‘skill-creator는 사용 안 하지만 언급하여 추천’으로 명시되어 있다. 표지 다음 2장에서 소개한다. 강의에서 실제 설치하거나 스킬 제작 실습을 추가하지 않는다.

화면: 작업 방식·결과물 예시 → skill-creator를 사용하는 에이전트 → 스킬 폴더(SKILL.md). 폴더 이름 라벨은 두지 않는다. 상품 소개글은 입력 예시로 대본에서만 짧게 연결. 회사 사규와 스킬을 함께 넣어 업무 결과물을 생성하는 그림과 구별한다.

원하는 업무에 맞는 스킬을 직접 만들 수 있다는 가능성을 소개한다. 한 번 생성한 초안이 완성된 품질을 보장한다고 설명하지 않는다. 새 요청에 적용해 보고 고치는 과정은 대본에서 짧게 다룬다.

커리큘럼 차이: course 저장소에는 Chapter 4가 3개 실습 클립, slide 저장소에는 2개 실습 클립으로 되어 있다. 이번 변경은 두 저장소에서 제목이 같은 Ch03-02에만 반영하며, Chapter 4 번호나 구성을 임의로 바꾸지 않는다.


## 2026-09-19 시각 규격

표지는 승인된 Part 4 교안의 상단 제목·부제, 본문의 핵심 선언과 관계 도식, 공통 로고 푸터로 구성한다. 제목만 중앙에 놓는 별도 표지 규격은 사용하지 않는다. 목차나 스킬 이름 목록은 표지에 넣지 않는다.

제목·본문·라벨·강조 문구는 템플릿의 역할별 타이포를 따른다. 표지뿐 아니라 모든 본문에서 같은 에이전트 SVG, 의미별 색, 관계를 나타내는 연결선을 사용한다. 강의 내용과 슬라이드 순서·개수는 유지한다.
