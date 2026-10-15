# Part 8 · Ch01-01 · 콘텐츠팀 구조 살펴보기 (R&R 분배)

## 주제 도출

- 한 줄 주제: 하나의 소재를 역할별로 나눠 블로그·카드뉴스·Threads를 만듭니다.
- 청중: 기획팀·영업팀·디자인팀 실습을 본 비개발자 수강생.
- 핵심 주장: 별도 소재 워커가 공통 자료를 준비한다 / 플랫폼 담당은 서로 다른 결과를 만든다 / 사람이 기준을 정하고 코디네이터가 배정·검수한다.
- 총 슬라이드 수: 8장. 사용자 승인한 공통·플랫폼별 자료 폴더 장은 7장, 콘텐츠팀 구조는 8장. 미채택 비교 2장 제거.
- 참고 실물: Part 7 Ch01-01의 1·2·3·9장, Part 6 Ch01-02의 도입 3장. 대본 골든셋 74.
- 사실 근거: 2026-10-14 최신 Part 8 실습 가이드와 ../⭐fastcampus-orca-projects/part8/platform-content-boilerplate의 README.md·AGENTS.md·prompts/produce.md를 직접 대조. 과거 수정 이력보다 현재 섹션과 최신 반영 기준을 우선한다.
- 색: 사람 gray, Coordinator yellow, 소재·블로그 brand, 인스타그램·이미지 하위 워커 purple, Threads green. 패턴 개념도의 역할·연결은 R&R green.
- 버릴 내용: 특정 모델 버전·추론 설정, 스킬 설치 명령, 다음 영상의 자세한 설정 절차.
- 검수: CSS grid로 주체 배치, 실제 DOM 기준으로 곡선 연결, 등장 시 좌표 이동 없음. 1920×1080·1280×800에서 전체와 재진입 확인.

## 슬라이드 1 / 8 — 콘텐츠팀 구조 살펴보기 (R&R 분배)

- 제목 키컬러: ‘콘텐츠팀 구조’. Part 5·6·7의 팀 구조 표지와 같은 의미 단위를 강조한다.

- 타입: COVER_SCENE
- 수강생의 질문: 이번 프로젝트에서 사람이 정하고 에이전트가 맡을 일은 무엇인가?
- 한 문장 답: 사람이 브랜드 기준을 정하고 콘텐츠팀이 소재 수집부터 플랫폼별 제작과 검수까지 맡는다.
- 근거: README.md 작업 흐름; AGENTS.md 입력 확인
- 부제: 하나의 소재를 역할별로 나눠 블로그·카드뉴스·Threads를 만듭니다.
- 애니메이션: data-anim-step 순서대로 주체 → 전달선 → 후속 주체 → 결과를 fade로 표시한다. 노드 위치는 고정하고 선의 끝점은 동일 DOM 기준점으로 계산한다.
- 발표 노트: 사람이 브랜드 기준을 정하고 콘텐츠팀이 소재 수집부터 플랫폼별 제작과 검수까지 맡는다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="scene scene--cover"><div class="scene__copy anim-item"><p class="statement">소재는 하나<strong>결과물은 플랫폼별로</strong></p></div><div class="scene__visual p8-map p8-covermap"><svg aria-hidden="true" class="p8-wires"><path class="anim-item" data-anim-step="2" data-axis="h" data-from="source" data-lane="0" data-offset="0" data-to="blog" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="2" data-axis="h" data-from="source" data-lane="0" data-offset="0" data-to="insta" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="2" data-axis="h" data-from="source" data-lane="0" data-offset="0" data-to="threads" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path></svg><div class="p8-actor tone-gray anim-item" data-anim-step="1" data-node="source"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-document"></use></svg><h2 class="heading">하나의 소재</h2></div><div class="p8-actor tone-brand anim-item" data-anim-step="3" data-node="blog"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-document"></use></svg><h2 class="heading">블로그</h2></div><div class="p8-actor tone-purple anim-item" data-anim-step="3" data-node="insta"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-cards"></use></svg><h2 class="heading">카드뉴스</h2></div><div class="p8-actor tone-green anim-item" data-anim-step="3" data-node="threads"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-social"></use></svg><h2 class="heading">Threads</h2></div></div></div></main>
```

## 슬라이드 2 / 8 — 플랫폼별 최종 결과물

- 타입: ARTIFACT_TRIPTYCH
- 수강생의 질문: 콘텐츠팀을 돌리면 무엇이 남는가?
- 한 문장 답: 이미지와 태그를 포함한 blog.md, 카드뉴스 이미지·캡션, Threads 원고를 각각 만든다.
- 근거: README.md 회차 결과물; 기존 케이크 이미지는 형태 예시로만 재사용
- 부제: 같은 소재로 블로그 글·인스타그램 카드뉴스·Threads 게시글을 완성합니다.
- 애니메이션: data-anim-step 순서대로 주체 → 전달선 → 후속 주체 → 결과를 fade로 표시한다. 노드 위치는 고정하고 선의 끝점은 동일 DOM 기준점으로 계산한다.
- 발표 노트: 이미지와 태그를 포함한 blog.md, 카드뉴스 이미지·캡션, Threads 원고를 각각 만든다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="p8-products">
<section class="p8-product tone-brand anim-item" data-anim-step="0"><h2 class="heading">블로그</h2><div class="p8-browser"><div class="p8-browser-bar"><i></i><i></i><i></i><span>소미의 주말 홈카페</span></div><div class="p8-blog"><span>딸기 디저트 레시피</span><h3>스트로베리 퐁당 케이크 만들기,<br/>성수동 감성 그대로</h3><img alt="스트로베리 퐁당 케이크 완성 사진" src="/artifacts/part8/_images/ch01-01-final-blog-hero.png"/><p>투명 컵 안에 딸기와 생크림을 층층이 쌓는<br/>30분 홈카페 디저트예요.</p></div></div><p class="copy">검색으로 찾아 읽는 정보성 긴 글</p></section>
<section class="p8-product tone-purple anim-item" data-anim-step="0"><h2 class="heading">인스타그램</h2><div class="p8-card-art"><img alt="스트로베리 퐁당 케이크 카드뉴스 표지" src="/artifacts/part8/_images/ch01-01-final-instagram.png"/></div><p class="copy">이미지로 한눈에 보여주는 게시물</p></section>
<section class="p8-product tone-green anim-item" data-anim-step="0"><h2 class="heading">Threads</h2><div class="p8-thread"><div class="p8-thread-profile"><span></span><strong>소미의 주말 홈카페</strong></div><p>다이어트 중인데 이 컵 보고 그냥 무너졌다..</p><p>딸기랑 생크림을 이렇게 층층이 쌓아놓으면 어떻게 참아🍓🤍</p><p>스트로베리 퐁당 케이크, 나만 알기 아까워서 레시피 남겨둠.<br/>저장 필수.</p><svg aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 150 24"><path d="M12 21 3 12C-3 3 9-2 12 5 16-2 28 3 21 12Z M51 3a9 9 0 1 1-5 16l-7 3 2-7a9 9 0 0 1 10-12Z M79 6h17l-4-4m4 4-4 4 M96 18H79l4 4m-4-4 4-4 M120 4l23 8-23 8 5-8Z"></path></svg></div><p class="copy">바로 읽히는 짧은 글</p></section>
</div></main>
```

## 슬라이드 3 / 8 — 콘텐츠팀 협업 패턴

- 타입: ROLE_DISTRIBUTION
- 수강생의 질문: 콘텐츠팀은 어떤 협업 패턴으로 일하는가?
- 한 문장 답: 하나의 소재를 서로 다른 역할에 나누고 각 결과를 모두 사용하는 R&R 분배다.
- 근거: Part 5 ch01-01-collaboration-patterns 8장 역할별 분담 도식, Part 6·7 팀 소개 3장 중앙 배치.
- 화면: 같은 소재 → 역할 A·B → 결과 A·B. 입력 purple, 역할·연결·결과 green.
- 애니메이션: 입력 1 → 역할·분기선 2 → 결과 3 → 정의 4.

```html
<main class="slide__body"><div class="team-pattern-layout"><div class="team-pattern-map" data-overview="roles"><svg aria-hidden="true" class="dependency-wires anim-item" data-anim-step="2"></svg><figure class="dependency-node anim-item is-input" data-anim-step="1" data-dependency-node="input" style="left:50%;top:10%"><div class="dependency-symbol"><svg aria-hidden="true" class="dependency-document" viewBox="0 0 88 100"><path class="document-page" d="M16 4H56L76 24V96H16Z"></path><path class="document-fold" d="M56 4V24H76"></path><path class="document-lines" d="M30 43H61M30 57H61M30 71H51"></path></svg></div><figcaption>같은 소재</figcaption></figure><figure class="dependency-node anim-item is-agent" data-anim-step="2" data-dependency-node="a" style="left:20%;top:45%"><div class="dependency-symbol"><svg aria-hidden="true" class="icon icon--robot" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewBox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg></div><figcaption>역할 A</figcaption></figure><figure class="dependency-node anim-item is-agent" data-anim-step="2" data-dependency-node="b" style="left:80%;top:45%"><div class="dependency-symbol"><svg aria-hidden="true" class="icon icon--robot" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewBox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg></div><figcaption>역할 B</figcaption></figure><figure class="dependency-node anim-item is-output" data-anim-step="3" data-dependency-node="oa" style="left:20%;top:88%"><div class="dependency-symbol"><svg aria-hidden="true" class="dependency-document" viewBox="0 0 88 100"><path class="document-page" d="M16 4H56L76 24V96H16Z"></path><path class="document-fold" d="M56 4V24H76"></path><path class="document-lines" d="M30 43H61M30 57H61M30 71H51"></path></svg></div><figcaption>결과 A</figcaption></figure><figure class="dependency-node anim-item is-output" data-anim-step="3" data-dependency-node="ob" style="left:80%;top:88%"><div class="dependency-symbol"><svg aria-hidden="true" class="dependency-document" viewBox="0 0 88 100"><path class="document-page" d="M16 4H56L76 24V96H16Z"></path><path class="document-fold" d="M56 4V24H76"></path><path class="document-lines" d="M30 43H61M30 57H61M30 71H51"></path></svg></div><figcaption>결과 B</figcaption></figure></div></div><p class="team-pattern-definition anim-item" data-anim-step="4">같은 소재를 서로 다른 역할이 받아, 각자의 결과물을 만듭니다.</p></main>
```

## 슬라이드 4 / 8 — 브랜드 기준 만들기

- 2026-10-14 추가 수정: 오른쪽 브랜드 기준을 Ch03-01 5장과 같은 접힌 모서리·항목·문서 하단 줄이 있는 문서형으로 변경한다. 호버 효과 없음. 문구·기존 흐름·화살표 정렬 유지.

- 타입: INPUT_AGENT_RULES
- 수강생의 질문: 브랜드 공통 기준은 무엇인가?
- 한 문장 답: 브랜드의 정체성·대상 독자·말투·콘텐츠 전략을 사람이 확인해 확정한다. 플랫폼별 포맷은 별도 자료로 구분한다.
- 근거: 가이드 2·3절; README.md artifacts/rules/ 문서
- 부제: 소재를 찾기 전에 내 브랜드의 독자·말투·전략을 먼저 정합니다.
- 애니메이션: 의미 묶음은 위치 고정 페이드로 순차 표시하며 하단 마무리는 본문 등장 뒤 표시한다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="p8-channel p8-map"><svg aria-hidden="true" class="p8-wires"><path class="anim-item" data-anim-step="1" data-axis="h" data-from="person" data-lane="0" data-offset="0" data-to="main" marker-end="url(#p8-tip-gray)" stroke="var(--gray)"></path><path class="anim-item" data-anim-step="3" data-axis="h" data-from="main" data-lane="0" data-offset="0" data-to="rules" marker-end="url(#p8-tip-brand)" stroke="var(--brand)"></path></svg><div class="p8-actor tone-gray anim-item" data-anim-step="0" data-node="person"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-person"></use></svg><div class="p8-actor-copy"><h2 class="heading">사람</h2><p class="copy">인터뷰 답변 · 기존 글</p></div></div><div class="p8-actor tone-yellow anim-item" data-anim-step="2" data-node="main"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Agent</h2><p class="copy">인터뷰 · 전략 제안</p></div></div><section class="flow-artifact shape-paper tone-brand anim-item p8-channel-rules" data-anim-step="4" data-node="rules"><span class="paper-fold" aria-hidden="true"></span><h2 class="heading">브랜드 기준</h2><ul class="p8-channel-lines"><li class="copy">브랜드 정체성 · 대상 독자</li><li class="copy">말투 · 표현 규칙</li><li class="copy">콘텐츠 전략</li></ul><div class="artifact-decoration" aria-hidden="true"><div class="paper-rules"><i></i><i></i><i></i></div></div></section></div><p class="p8-note copy anim-item" data-anim-step="6">내 확인을 거쳐 저장한 브랜드 기준을 매 회차 소재 수집과 제작에 재사용합니다.</p></main>

```

## 슬라이드 5 / 8 — 제작 전 소재 준비

- 타입: TASK_DEPENDENCY
- 수강생의 질문: 소재는 누가 고르고 브리프는 누가 만드는가?
- 한 문장 답: 소재 수집 워커가 후보 수집·소재 선정·브리프 작성을 맡고, 코디네이터가 확인해 세 플랫폼 워커에게 전달한다. 지정 소재 실습은 오케스트레이션 전에 브리프를 만든다.
- 근거: 가이드 7·8절; prompts/produce.md 작업 배정 1·2
- 부제: 소재 수집 워커가 후보를 모아 소재를 고르고, 브리프를 작성해 코디네이터에게 보고합니다.
- 애니메이션: 의미 묶음은 위치 고정 페이드로 순차 표시하며 하단 마무리는 본문 등장 뒤 표시한다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="p8-prep p8-map"><svg aria-hidden="true" class="p8-wires"><path class="anim-item" data-anim-step="1" data-axis="h" data-from="material" data-lane="0" data-offset="0" data-to="brief" marker-end="url(#p8-tip-brand)" stroke="var(--brand)"></path><path class="anim-item" data-anim-step="3" data-axis="h" data-from="brief" data-lane="0" data-offset="0" data-to="blog" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="3" data-axis="h" data-from="brief" data-lane="0" data-offset="0" data-to="insta" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="3" data-axis="h" data-from="brief" data-lane="0" data-offset="0" data-to="threads" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="5" data-axis="h" data-from="blog" data-lane="0" data-offset="0" data-to="blogout" marker-end="url(#p8-tip-brand)" stroke="var(--brand)"></path><path class="anim-item" data-anim-step="5" data-axis="h" data-from="insta" data-lane="0" data-offset="0" data-to="instaout" marker-end="url(#p8-tip-purple)" stroke="var(--purple)"></path><path class="anim-item" data-anim-step="5" data-axis="h" data-from="threads" data-lane="0" data-offset="0" data-to="threadsout" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path></svg><div class="p8-actor tone-brand anim-item" data-anim-step="0" data-node="material"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">소재 수집 워커</h2><p class="copy">후보·출처 수집<br>소재 선정 · 브리프 작성</p></div></div><div class="p8-actor tone-gray anim-item" data-anim-step="2" data-node="brief"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-document"></use></svg><div class="p8-actor-copy"><h2 class="heading">소재 브리프</h2><p class="copy">코디네이터 확인·전달<br>핵심 사실 · 출처 링크</p></div></div><div class="p8-actor tone-brand anim-item" data-anim-step="4" data-node="blog"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">블로그 워커</h2><p class="copy"></p></div></div><div class="p8-actor tone-purple anim-item" data-anim-step="4" data-node="insta"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">인스타그램 워커</h2><p class="copy"></p></div></div><div class="p8-actor tone-green anim-item" data-anim-step="4" data-node="threads"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Threads 워커</h2><p class="copy"></p></div></div><div class="p8-actor tone-brand anim-item" data-anim-step="5" data-node="blogout"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-document"></use></svg><div class="p8-actor-copy"><h2 class="heading">블로그 글</h2></div></div><div class="p8-actor tone-purple anim-item" data-anim-step="5" data-node="instaout"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-cards"></use></svg><div class="p8-actor-copy"><h2 class="heading">카드뉴스</h2></div></div><div class="p8-actor tone-green anim-item" data-anim-step="5" data-node="threadsout"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-social"></use></svg><div class="p8-actor-copy"><h2 class="heading">게시글</h2></div></div></div><p class="p8-note copy anim-item" data-anim-step="7">지정 소재는 수집 워커 없이, 오케스트레이션 전에 브리프를 준비합니다.</p></main>

```

## 슬라이드 6 / 8 — 소재 선정 기준

- 타입: OPEN_TRIPTYCH
- 수강생의 질문: 소재 담당은 어떤 기준으로 후보를 고르는가?
- 한 문장 답: 독자 가치·브랜드 적합성·출처 신뢰성을 검토하고, 구체적인 선정 기준은 브랜드의 콘텐츠 전략에서 정한다.
- 근거: 2026-10-12 사용자 요청으로 Ch02-01에서 이동한 장 보존; 실습 가이드 소재 선정 기준
- 부제: 독자에게 줄 가치와 브랜드의 방향, 출처의 신뢰성을 바탕으로 소재를 고릅니다.
- 애니메이션: 독자 가치 → 브랜드 적합성 → 출처 신뢰성 순서로 의미 묶음을 표시한다. 기존 세 열 레이아웃과 페이드 규칙을 유지한다.
- 발표 노트: 독자 가치·브랜드 적합성·출처 신뢰성을 검토하고, 구체적인 선정 기준은 브랜드의 콘텐츠 전략에서 정한다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="triptych content b3-triptych"><section class="concept anim-item"><svg aria-hidden="true" class="tx-art tone-brand" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-person"></use></svg><h2 class="heading tone-brand">독자 가치</h2><p class="copy">독자가 읽고<br>활용할 이유가 있는가</p></section><section class="concept anim-item"><svg aria-hidden="true" class="tx-art tone-purple" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-cards"></use></svg><h2 class="heading tone-purple">브랜드 적합성</h2><p class="copy">브랜드의 주제와<br>목적에 맞는가</p></section><section class="concept anim-item"><svg aria-hidden="true" class="tx-art tone-green" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewBox="0 0 100 100"><use href="#shape-document"></use></svg><h2 class="heading tone-green">출처 신뢰성</h2><p class="copy">핵심 사실을<br>출처로 확인할 수 있는가</p></section></div></main>
```

## 슬라이드 7 / 8 — 공통 자료와 콘텐츠 포맷

- 타입: OBJECT_DETAIL_COMPARE
- 수강생의 질문: 세 문서 중 무엇을 함께 보고, 무엇을 담당 플랫폼별로 보는가?
- 한 문장 답: 모든 워커가 브랜드 기준과 소재 브리프를 공유하고, 자기 플랫폼의 콘텐츠 포맷을 선택한다.
- 부제: 브랜드 기준과 소재 브리프는 함께 보고, 콘텐츠 포맷은 담당 플랫폼에 맞춰 선택합니다.
- 디자인: 양쪽 모두 같은 외곽·탭·높이·안쪽 여백의 자료 폴더. 왼쪽 공통 자료 폴더에는 브랜드 기준과 소재 브리프, 오른쪽 플랫폼별 자료 폴더에는 콘텐츠 포맷 문서를 넣는다. ‘공통으로 공유 / 플랫폼별로 선택’ 두 범위를 대비한다. 공통 폴더 내부에는 브랜드 기준과 소재 브리프를 같은 높이로 배치한다.
- 호버: 개별 문서의 색은 유지하고, 문서를 포함한 폴더 영역에 포인터가 들어오면 폴더 외곽·배경·탭을 묶어서 강조한다.
- 내용: 승인한 세 문서 내용을 보존하며 공통 여부에 따라 두 범위로 재배치한다. 브랜드 기준 brand, 소재 브리프 purple, 콘텐츠 포맷 green을 유지한다.
- 애니메이션: 공통 묶음 전체(step 0)가 완전히 보인 뒤 콘텐츠 포맷(step 2), 마지막에 핵심 문장(step 4). 중첩 애니메이션 없음.
- 승인: 2026-10-14 사용자가 이전 8장의 폴더 비교·폴더 호버를 최종 승인했다. 미채택 이전 7·9장은 제거하며 현재 장은 7장으로 이동한다.

```html
<main class="slide__body tx-body b3-body p8-body"><div class="p8-scope-compare"><section class="p8-shared-scope anim-item" data-anim-step="0"><h2 class="p8-scope-heading">공통으로 공유</h2><div class="p8-document-folder"><section class="flow-artifact shape-paper p8-scope-paper p8-scope-channel"><span class="paper-fold" aria-hidden="true"></span><div class="artifact-chrome">회차마다 재사용</div><h3 class="heading">브랜드 기준</h3><ul><li class="copy">브랜드 프로필 · 말투 규칙</li><li class="copy">콘텐츠 전략</li><li class="copy">소재 선정 · 수집 범위</li><li class="copy">소재 브리프 작성 기준</li></ul><div class="artifact-decoration" aria-hidden="true"><div class="paper-rules"><i></i><i></i><i></i></div></div></section><section class="flow-artifact shape-paper p8-scope-paper p8-scope-brief"><span class="paper-fold" aria-hidden="true"></span><div class="artifact-chrome">이번 회차의 소재</div><h3 class="heading">소재 브리프</h3><ul><li class="copy">회차 목적 · 콘텐츠 유형</li><li class="copy">대상 독자 · 핵심 메시지</li><li class="copy">핵심 사실 · 출처 링크</li><li class="copy">피할 표현</li></ul><div class="artifact-decoration" aria-hidden="true"><div class="paper-rules"><i></i><i></i><i></i></div></div></section></div></section><section class="p8-platform-scope anim-item" data-anim-step="2"><h2 class="p8-scope-heading">플랫폼별로 선택</h2><div class="p8-document-folder p8-format-slot"><section class="flow-artifact shape-paper p8-scope-paper p8-scope-format"><span class="paper-fold" aria-hidden="true"></span><div class="artifact-chrome">담당 플랫폼</div><h3 class="heading">콘텐츠 포맷</h3><ul><li class="copy">블로그 · 카드뉴스 · Threads</li><li class="copy">플랫폼별 전개 구조</li><li class="copy">분량 · 이미지 · 태그</li><li class="copy">선택한 포맷의 샘플</li></ul><div class="artifact-decoration" aria-hidden="true"><div class="paper-rules"><i></i><i></i><i></i></div></div></section></div></section></div><p class="p8-note copy anim-item" data-anim-step="4">같은 사실과 말투를 유지하면서, 구성과 표현은 플랫폼에 맞게 달라집니다.</p></main>
```

## 슬라이드 8 / 8 — 콘텐츠팀의 구조

- 타입: DELEGATION_HIERARCHY
- 수강생의 질문: 사람·코디네이터·워커가 각각 무엇을 맡는가?
- 한 문장 답: 사람은 기준·포맷 확정과 결과 확인, 소재 수집 워커는 수집·선정·브리프 작성, 코디네이터는 배정·브리프 확인과 전달·결과 확인을 맡는다. 제작 워커는 블로그 글·카드뉴스·Threads 게시글을 만들고 블로그 이미지 생성은 Codex 하위 워커에게 맡긴다.
- 근거: 가이드 2~8절; prompts/produce.md 전체; AGENTS.md 결과 확인·완료 기준
- 부제: 소재 수집 워커가 고른 소재의 브리프를 코디네이터가 확인·전달하고, 플랫폼별 제작을 배정합니다.
- 애니메이션: 의미 묶음은 위치 고정 페이드로 순차 표시하며 하단 마무리는 본문 등장 뒤 표시한다.

**화면 요소·관계 확정**

```html
<main class="slide__body tx-body b3-body p8-body"><div class="p8-team p8-map"><svg aria-hidden="true" class="p8-wires"><path class="anim-item" data-anim-step="1" data-axis="h" data-from="person" data-lane="-20" data-offset="0" data-relation="assign" data-to="coord" marker-end="url(#p8-tip-yellow)" stroke="var(--yellow)"></path><path class="anim-item" data-anim-step="6" data-axis="h" data-from="coord" data-lane="20" data-offset="0" data-relation="result" data-to="person" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="2" data-axis="h" data-from="coord" data-lane="-20" data-offset="0" data-relation="assign" data-to="material" marker-end="url(#p8-tip-yellow)" stroke="var(--yellow)"></path><path class="anim-item" data-anim-step="3" data-axis="h" data-from="material" data-lane="20" data-offset="0" data-relation="report" data-to="coord" marker-end="url(#p8-tip-brand)" stroke="var(--brand)"></path><path class="anim-item" data-anim-step="4" data-axis="v" data-from="coord" data-lane="0" data-offset="-45" data-relation="assign" data-to="blog" marker-end="url(#p8-tip-yellow)" stroke="var(--yellow)"></path><path class="anim-item" data-anim-step="5" data-axis="up" data-from="blog" data-lane="0" data-offset="-25" data-relation="report" data-to="coord" marker-end="url(#p8-tip-brand)" stroke="var(--brand)"></path><path class="anim-item" data-anim-step="4" data-axis="v" data-from="coord" data-lane="0" data-offset="-10" data-relation="assign" data-to="insta" marker-end="url(#p8-tip-yellow)" stroke="var(--yellow)"></path><path class="anim-item" data-anim-step="5" data-axis="up" data-from="insta" data-lane="0" data-offset="10" data-relation="report" data-to="coord" marker-end="url(#p8-tip-purple)" stroke="var(--purple)"></path><path class="anim-item" data-anim-step="4" data-axis="v" data-from="coord" data-lane="0" data-offset="25" data-relation="assign" data-to="threads" marker-end="url(#p8-tip-yellow)" stroke="var(--yellow)"></path><path class="anim-item" data-anim-step="5" data-axis="up" data-from="threads" data-lane="0" data-offset="45" data-relation="report" data-to="coord" marker-end="url(#p8-tip-green)" stroke="var(--green)"></path><path class="anim-item" data-anim-step="5" data-axis="v" data-from="blog" data-lane="0" data-offset="0" data-relation="assign" data-to="child" marker-end="url(#p8-tip-purple)" stroke="var(--purple)"></path></svg><div class="p8-actor tone-gray anim-item" data-anim-step="0" data-node="person"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 100 100"><use href="#shape-person"></use></svg><div class="p8-actor-copy"><h2 class="heading">사람</h2><p class="copy">브랜드 기준·포맷 확정 · 결과 확인</p></div></div><div class="p8-actor tone-yellow anim-item" data-anim-step="1" data-node="coord"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">코디네이터</h2><p class="copy">브리프 확인·전달 · 제작 배정</p></div></div><div class="p8-actor tone-brand anim-item" data-anim-step="2" data-node="material"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">소재 수집 워커</h2><p class="copy">소재 수집·선정 · 브리프 작성</p></div></div><div class="p8-actor tone-brand anim-item" data-anim-step="4" data-node="blog"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">블로그 워커</h2><p class="copy">Claude Code · 블로그 글</p></div></div><div class="p8-actor tone-purple anim-item" data-anim-step="4" data-node="insta"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">인스타그램 워커</h2><p class="copy">Codex · 카드뉴스</p></div></div><div class="p8-actor tone-green anim-item" data-anim-step="4" data-node="threads"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Threads 워커</h2><p class="copy">Hermes · Threads 게시글</p></div></div><div class="p8-actor tone-purple anim-item p8-child" data-anim-step="5" data-node="child"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">이미지 하위 워커</h2><p class="copy">Codex · 블로그 이미지</p></div></div><span class="p8-route-label p8-person-request anim-item tone-yellow" data-anim-step="1">요청 · 브랜드 기준</span><span class="p8-route-label p8-person-result anim-item tone-green" data-anim-step="6">콘텐츠 3종</span><span class="p8-route-label p8-material-request anim-item tone-yellow" data-anim-step="2">소재 수집 배정</span><span class="p8-route-label p8-material-result anim-item tone-brand" data-anim-step="3">소재 후보 · 브리프</span></div></main>

```

## 2026-10-12 3차 수정 구성

- 2장: 원본 최종 preview.html에 연결된 블로그·Blue Diner 카드뉴스 표지·Threads B안의 실제 화면을 사용한다. 카드뉴스는 한 장만 표시하며 모두 같은 프레임 규격을 쓴다. 임의로 만든 문구는 제거한다. 원본 최종 결과물 열기 링크를 제공한다.
- 3장: 워커는 블로그 brand·인스타그램 purple·Threads green으로 구분한다. 산출물 아이콘도 담당 색을 따른다. 선의 양끝과 아이콘 사이 여백을 40~48px로 넓히고 도식 최대폭을 제한한다.
- 4장: 중복 설명이므로 삭제 여부를 사용자에게 확인 중이다. 답변 전에는 그대로 유지한다.
- 5장: 본문 grid에 빈 auto 행을 만들지 않고 항목 묶음을 본문 중앙에 배치한다.
- 7장: 양쪽 공통 입력 step 0 → 연결선 step 1 → 결과물 step 2 → 선택/사용 step 3. 애니메이션을 가진 부모 안에 자식 애니메이션을 중첩하지 않는다.
- 기존 8장: 사용자 요청대로 현재 형태를 보존한다.
- 추가 수평 후보: 사람 → Coordinator(수집 배정) → 소재 수집 워커(소재 브리프 보고) → 같은 Coordinator(브리프 확인·워커 기동) → 플랫폼별 워커로 연결한다. 같은 코디네이터의 두 시점을 표시하며 수집 워커에서 제작 워커로 직접 연결하지 않는다.
- 후보 부제: 소재 브리프를 받은 코디네이터가 플랫폼별 워커를 띄웁니다.
- 후보 하단: 같은 Coordinator가 소재 수집 배정과 플랫폼별 워커 기동을 이어서 맡습니다.
- 대본은 후보 선택·덱 승인 전 갱신하지 않는다.

## 철회된 후보 기록 — 콘텐츠팀의 수평 구조

- 타입: DELEGATION_HIERARCHY의 수평 진행 변형
- 핵심: 브리프를 받는 주체와 플랫폼별 워커를 띄우는 주체는 같은 코디네이터다.
- 근거: 2026-10-12 사용자 추가 지시. 최신 프로젝트 요청문과 다른 역할 분배는 이 후보에서 사용자 지시를 우선한다.
- 등장: 사람 0 → 배정 Coordinator 1 → 수집 워커 2 → 브리프 확인 Coordinator 3 → 플랫폼 워커 4 → 하단 설명 5.

```html
<div class="p8-horizontal p8-map"><svg class="p8-wires" aria-hidden="true"><path class="anim-item" data-from="person" data-to="assign" data-axis="h" data-lane="0" data-offset="0" data-anim-step="1" stroke="var(--yellow)" marker-end="url(#p8-tip-yellow)"/><path class="anim-item" data-from="assign" data-to="material" data-axis="h" data-lane="0" data-offset="0" data-anim-step="2" stroke="var(--yellow)" marker-end="url(#p8-tip-yellow)"/><path class="anim-item" data-from="material" data-to="launch" data-axis="h" data-lane="0" data-offset="0" data-anim-step="3" stroke="var(--brand)" marker-end="url(#p8-tip-brand)"/><path class="anim-item" data-from="launch" data-to="blog" data-axis="h" data-lane="0" data-offset="0" data-anim-step="4" stroke="var(--yellow)" marker-end="url(#p8-tip-yellow)"/><path class="anim-item" data-from="launch" data-to="insta" data-axis="h" data-lane="0" data-offset="0" data-anim-step="4" stroke="var(--yellow)" marker-end="url(#p8-tip-yellow)"/><path class="anim-item" data-from="launch" data-to="threads" data-axis="h" data-lane="0" data-offset="0" data-anim-step="4" stroke="var(--yellow)" marker-end="url(#p8-tip-yellow)"/></svg><div class="p8-actor tone-gray anim-item" data-node="person" data-anim-step="0"><svg class="p8-icon" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><use href="#shape-person"/></svg><div class="p8-actor-copy"><h2 class="heading">사람</h2><p class="copy">채널 기준 · 요청</p></div></div><div class="p8-actor tone-yellow anim-item" data-node="assign" data-anim-step="1"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Coordinator</h2><p class="copy">소재 수집 배정</p></div></div><div class="p8-actor tone-brand anim-item" data-node="material" data-anim-step="2"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">소재 수집 워커</h2><p class="copy">소재 선정<br>브리프 보고</p></div></div><div class="p8-actor tone-yellow anim-item" data-node="launch" data-anim-step="3"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Coordinator</h2><p class="copy">브리프 확인<br>플랫폼 워커 기동</p></div></div><div class="p8-actor tone-brand anim-item" data-node="blog" data-anim-step="4"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">블로그 워커</h2><p class="copy">Claude Code</p></div><div class="p8-horizontal-child tone-purple"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><span>이미지 하위 워커<br>Codex</span></div></div><div class="p8-actor tone-purple anim-item" data-node="insta" data-anim-step="4"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">인스타그램 워커</h2><p class="copy">Codex</p></div></div><div class="p8-actor tone-green anim-item" data-node="threads" data-anim-step="4"><svg aria-hidden="true" class="p8-icon" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 56 58"><rect fill="var(--text)" height="38" rx="18" stroke="var(--gray)" width="50" x="3" y="3"></rect><rect fill="var(--bg)" height="11" rx="5.5" stroke="none" width="34" x="11" y="16"></rect><path d="M18 21.5H38" stroke-width="3.5"></path><path d="M13 42C7 45 7 52 7 55H49C49 52 49 45 43 42"></path></svg><div class="p8-actor-copy"><h2 class="heading">Threads 워커</h2><p class="copy">Hermes</p></div></div></div><p class="p8-note copy anim-item" data-anim-step="5">같은 Coordinator가 소재 수집 배정과 플랫폼별 워커 기동을 이어서 맡습니다.</p>
```

## 2026-10-12 4차 수정 — 8장 구조 유지

- 수평 후보는 철회한다. 최종 덱은 8장이고 Coordinator는 구조도에 한 번만 표시한다.
- 기존 8장의 사람·코디네이터·소재 수집·제작 워커 배치를 유지한다. 배정·전달은 실선, 모든 결과 보고는 점선으로 통일한다. 소재 브리프 보고도 예외 없이 점선이다.
- Coordinator: 소재 브리프 전달 / 제작 워커 기동 / 결과 확인·취합. 점수 평가를 뜻하는 용어는 사용하지 않는다.
- 워커별 결과물은 블로그 글·HTML, 카드뉴스·캡션, Threads 게시글로 별도 표시한다.
- 2장은 브라우저 형태 블로그, 실제 이미지 카드뉴스 한 장, 실제 Threads 글로 표현한다. 결과물 링크는 제거한다.

## 2026-10-12 5차 수정 구성

- 패턴과 프로젝트 적용 도식을 분리한다. 협업 패턴은 지정된 Part 5 8장의 오른쪽 도식을 그대로 가져오고 Part 6·7 팀 소개 장과 같은 중앙 배치·정의 규격을 적용한다.
- 현재 3장의 원래 기록상 제목은 “플랫폼별 결과물”. 현재 그림의 핵심은 같은 소재 브리프 → 플랫폼별 담당 → 각 결과물이므로 “플랫폼별 역할 분담”으로 바꾸어 4장에 둔다.
- 2장 캡션은 임의의 마케팅 목적 대신 실제 담긴 내용으로 쓴다. 재료·계량·만드는 순서 / 완성 사진·핵심 과정 / 짧은 감상·레시피 소개.
- 2장의 인스타그램 카드 이미지 자체에 다른 두 제품과 같은 border-radius를 적용한다.

### 5차 추가 정정

- 병렬 실행과 차이(기존 7장, 현재 8장): 동시에 보이라는 요청이 아니었다. 왼쪽 등장 완료 후 오른쪽 순차 등장. 1410ms에 왼쪽 완료, 1450ms에 오른쪽 시작으로 공백 40ms.
- 콘텐츠팀의 구조(기존 8장, 현재 9장): Part 6·7처럼 주체별 설명 한 줄, 연결 라벨, 하단 한 줄로 정리한다. 범례와 중복 설명 삭제.
- 사람에게 전달하는 선은 실선이며 라벨은 “콘텐츠 3종”. 워커→Coordinator의 브리프·제작 결과 보고만 점선이다.

## 2026-10-12 6차 수정 구성

- 사용자 요청: 4·5장의 차이는 워커별 결과물 표시 여부뿐이므로 합친다. 기존 5장 “제작 전 소재 준비”를 기본으로 각 워커의 결과물을 붙인다.
- 새 4장: 소재 수집 워커 → 소재 브리프 → 플랫폼별 워커 → 각 결과물. 기존 5장의 제목·설명·소재 준비 구조를 유지하며 기존 4장의 결과물 아이콘과 이름을 오른쪽에 붙인다.
- 블로그 워커 → 블로그 글, 인스타그램 워커 → 카드뉴스, Threads 워커 → 게시글. 결과물은 각 담당의 색을 유지한다.
- 기존 4장은 삭제하고 기존 5~9장이 4~8장으로 이동한다. 총 8장.

## 2026-10-12 7차 수정

- 8장의 하단 설명을 삭제하고 본문을 단일 행으로 확장. 블로그 워커와 이미지 하위 워커 사이에 min(4rem,9cqh) 여백을 확보한다.

## 2026-10-12 10차 수정 구성

- 근거: 사용자 지정 실습자료 ../fastcampus-orca-course/edu-note/output/[Part 8] 플랫폼별 콘텐츠 자동화 시스템 구축 가이드.md, 프로젝트 prompts/produce.md.
- 새 4장 “채널 기준 만들기”: 사람의 인터뷰 답변·기존 글 → 메인 에이전트의 인터뷰·전략 제안 → 채널 기준(프로필·말투, 콘텐츠 전략·소재 수집 범위, 공통 전달 기준, 플랫폼별 포맷·샘플). 처음 한 번 사용자 확인 후 저장하고 회차마다 재사용.
- 소재 준비는 5장으로 이동. 인스타그램 계정의 최근 게시물·탐색 추천 게시물에서 반응이 있는 소재 후보를 찾고 원문 근거를 수집하는 역할을 명시. “최신 인기글” 같은 확인되지 않은 순위 표현은 사용하지 않는다.
- 자료의 실제 책임 분배: 수집 워커는 후보·근거 수집, 코디네이터는 소재 선택·브리프 확정. 5장·7장 공통 기준 설명·9장 팀 구조에서 동일하게 정정.
- 수집하는 채널은 전략의 수집 범위로 정한다. 인스타그램 연결 시 최근·추천 게시물, 이외 웹·블로그·Threads도 수집 도구의 대상이다. 본 장에서는 사용자 요청의 인스타그램을 설명한다.
- 전체 9장.

## 2026-10-13 11차 수정 구성

- 근거: 사용자 방향 변경으로 Part 8에서 인스타그램 직접 수집을 제거하고, 소재 수집 Claude 워커가 하네스 기본 웹 검색으로 공개 글·자료의 후보·근거를 모으도록 실습자료·프로젝트 `prompts/produce.md`를 수정했다.
- 텍스트만 최소 수정(레이아웃·애니메이션·다른 장 변경 없음): 5장 부제를 “콘텐츠 전략의 수집 범위를 웹 검색해 소재 후보와 근거를 모읍니다.”로, 5장 소재 수집 워커 설명을 “공개 글·자료 검색 / 웹 검색 · 후보와 근거”로, 9장 소재 수집 워커 설명을 “웹 검색 후보·근거 수집”으로 바꿨다. 위 10차의 인스타그램 수집 설명은 이 수정으로 대체한다.

## 2026-10-13 11차 수정

- 4장 두 화살표를 같은 중앙선의 수평 직선으로 변경. 사람·Agent 아이콘과 채널 기준 문서의 세로 중앙을 일치시킴.
- 메인 에이전트 → Agent. “처음 한 번 만들어 둘 문서” 삭제.
- 제목은 “채널 기준” 전체를 키컬러로 강조하고 해당 문서·연결선도 brand로 통일. 7장에서도 채널 기준은 brand, 소재 브리프는 purple로 구별. 7장 제목 강조는 “공통 기준”으로 정리.


## 2026-10-13 설계 정합성 수정

- 5·9장: 소재 수집 워커가 후보·출처를 수집하고 코디네이터가 고른 소재로 브리프를 작성한다. 코디네이터는 선택·브리프 확인·전달·제작 배정·결과 확인을 담당한다. 지정 소재 실행은 수집 워커 없이 오케스트레이션 전에 브리프를 준비한다.
- 7장: 브리프는 회차 목적, 대상 독자, 핵심 메시지, 핵심 사실과 출처 링크, 피할 표현으로 구성한다. 원문 기록은 material/raw/에 별도 저장하며 브리프 항목에서 제외한다.
- 6·8장: 소재 선정 기준과 플랫폼별 역할은 콘텐츠 전략에서 정한다. 화면의 레시피 기준과 역할은 예시임을 명시한다.
- 9장: 블로그 결과물은 이미지·태그가 포함된 blog.md. HTML 산출물 표현 제거.
- 용어: 출처·출처 링크, 콘텐츠 포맷·포맷 문서, 코디네이터, Threads로 통일한다.
- 2장의 블로그 브라우저 모양은 사용자 지정 미리보기 형식으로 유지한다. 최종 산출물 형식을 HTML로 설명하지 않는다.


## 2026-10-13 14차 — 중복 비교 장 삭제

- 앞선 클립과 이 덱 3장에서 설명한 패턴 비교를 반복하지 않도록 기존 8장 “병렬 실행과 차이” 삭제.
- “공통 기준과 조건” 다음에 “콘텐츠팀의 구조”를 바로 연결. 구조도는 현재 8장, 덱은 총 8장.

## 2026-10-14 6장 일반화

- 레시피 사례에 한정된 선정 기준 설명을 독자 가치·채널 적합성·출처 신뢰성으로 교체했다. 현재 6장은 예시 장이 아니며, 이전 이력의 레시피 예시 지시는 이 수정으로 대체한다.

## 2026-10-14 실습자료 전체 대조 — 최신 반영 기준

- 4장 공통 채널 기준과 플랫폼별 포맷 구분. 5·8장 소재 수집 워커의 수집·선정·브리프 작성 책임 반영. 7장 채널 기준·소재 브리프·콘텐츠 포맷을 세 묶음으로 분리. 사람은 기준·포맷 확정과 결과 확인, 워커 결과물은 동일한 수준의 이름으로 표시.
- 근거: 최신 Part 8 실습 가이드 2~8절과 platform-content-boilerplate의 README.md·AGENTS.md·prompts/produce.md.
- 이전 이력의 코디네이터 소재 선택·포맷을 공통 채널 기준 안에 넣는 설명보다 이번 수정이 우선한다.


2026-10-14 표기 통일: 4장 노드 라벨 Agent → 에이전트.

## 2026-10-15 용어 변경

- 사용자 지시로 세 플랫폼 공통 정체성을 가리키던 `채널`을 `브랜드`로 바꿨다(채널 기준→브랜드 기준, 채널 적합성→브랜드 적합성). 이전 이력의 `채널` 표기는 당시 기록으로 둔다.
