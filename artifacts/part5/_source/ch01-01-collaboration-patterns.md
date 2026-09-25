---
파트: part5
챕터: Chapter 1
클립: Ch01-01. 4가지 협업 패턴과 프로젝트 미리보기
길이: 10분
슬라이드: 12장
산출물: artifacts/part5/outputs/ch01-01-collaboration-patterns.html
상태: 작성중
---

# 4가지 협업 패턴과 프로젝트 미리보기

제작 목표: 업무에 맞는 역할과 연결 방식을 프로젝트로 살펴봅니다.

## 근거 자료

- `docs/curriculum.md`, `docs/course-brief.md`, `docs/confirmed-copy.md`, `docs/patterns.md`
- `../fastcampus-orca-course/edu-note/source/part5-7-practice-plan.md` 전체 흐름과 클립별 설명
- `../fastcampus-orca-course/project1-sidehustle-proposal/research-notes/market-research.md`
- `../fastcampus-orca-course/project1-sidehustle-proposal/item-candidates.md`
- `../fastcampus-orca-course/project1-sidehustle-proposal/proposal-template.md`
- `../fastcampus-orca-course/project1-sidehustle-proposal/quality-gate-criteria.md`
- `../fastcampus-orca-course/project1-sidehustle-proposal/final/proposal-final.md` 및 HTML

## 사실과 제작 범위

완성 프로젝트는 제작자의 설명 준비 자료다. 수강생에게 완성본의 근거를 역추적하는 과제를 주지 않는다. 상품과 리스크는 완성 프로젝트의 예시이며 현재 시장의 추천·수익 보장이 아니다. 기존 시장 조사 노트에는 공급가 등의 구체적인 출처 링크가 없어 새 조사의 정답으로 고정하지 않는다. 카테고리 등급과 세부 품목 점수의 변화에는 별도의 근거 확인이 필요하다.

Ch04-01~03은 일반 에이전트에게 개별 작업을 요청하고, Ch04-04는 품질 게이트 이론을 설명한다. Ch05-01 「단계별 품질 기준 정하기」(14분)는 시장 조사 노트·아이템 후보 비교표·판매 아이템 기획서의 단계별 통과·반려 기준을 정해 `artifacts/quality-gate/criteria.md`로 저장하는 실습만 한다. 프롬프트 작성·실행·반려 시연은 포함하지 않는다. Ch05-02 「목표 하나로 처음부터 끝까지 실행하기」(15분)는 강사가 제공한 프롬프트의 작업 순서·입출력·품질 기준 참조·반려/재검사 규칙을 이해한 뒤 바로 전체를 실행한다. 진행·검사·실제 반려 시 담당 워커의 수정 과정과 최종 세 문서를 확인한다. 프롬프트를 새로 작성하지 않으며, 반려를 만들기 위한 필수 오류 주입·사전 실행은 없다. 실제 반려 기록으로 설명하고 추가 연습은 본 실행 이후 선택사항이다. 코디네이터가 검사하며, 반려하면 원인 문서의 담당 워커가 수정하고 전체 기준을 재검사한다. 통과한 경우에만 다음 작업을 배정하고 상위 문서가 바뀌면 영향받는 후속 문서를 재확인한다. Part 5 같은 모델 기준 검사와 Part 6 다른 모델 교차 검증을 구분한다. 제작 중 상태이며 강사 확정·촬영 완료로 기록하지 않는다.

## Part 1 패턴·프로젝트 대조

`슬라이드-pdf/Part 01/Ch01-01. 강의 소개와 최종 결과물.pdf` 7장의 링크와 8장의 그림을 확인했다. PDF는 내용·그림 식별에만 사용했으며 새 HTML 레이아웃은 현재 스킬 기준으로 제작한다. PDF·KEY에서 이미지 추출이나 페이지 캡처 재사용은 하지 않았다.

원본은 저장소 Git `9e0f869`의 `artifacts/part1/_images/ch01-01-course-intro--pattern-*.png`다. Google Slides 전환 정리 커밋 `821bc69`로 삭제됐으나 원본 바이트를 Part 5 `_images/`로 복원했다. `artifacts/_maintenance/image-manifest.json` SHA256와 일치하며 상세는 `artifacts/_maintenance/pattern-image-provenance.json`에 남겼다.

| 원본 파일 | 사용 위치 |
|---|---|
| pattern-1-sequential.png | Ch01-01 6·12장 / Ch02-02 표지 |
| pattern-2-cross-check.png | Ch01-01 7장 |
| pattern-3-parallel.png | Ch01-01 8장 |
| pattern-4-rnr.png | Ch01-01 9장 |

- [판매 아이템 기획서](https://fastcampus-orca-course.vercel.app/project1-sidehustle-proposal/final/proposal-final.html): 차박용 접이식 미니 수납함의 선정 근거·실행 로드맵·예산·리스크
- [무브펫 제안·견적서](https://fastcampus-orca-course.vercel.app/project2-ads-proposal/final/proposal-quote-final.html): 자동 순환 급수기 광고 운영 제안, Codex 작성·Claude Code 평가
- [무드온 시안 비교](https://fastcampus-orca-course.vercel.app/project3-blackfriday-landing/final/preview.html): 동일 브리프에서 Claude 포스터형·Codex 룩북형
- [레시피 콘텐츠](https://fastcampus-orca-course.vercel.app/project4-recipe-content/final/preview.html): 스트로베리 퐁당 케이크의 블로그·카드뉴스·스레드

링크와 동일 경로의 형제 저장소 완성 HTML을 열어 내용을 확인했다. 공개본을 새로 배포하지 않는다.

## 화면 구성


### 1. 4가지 협업 패턴과 프로젝트 미리보기

역할: COVER_SCENE

> 업무에 맞는 역할과 연결 방식을 프로젝트로 살펴봅니다.

화면 문구·요소:
```json
{
  "image": "ch01-01-collaboration-patterns--cover-team-transparent.png",
  "composition": "사용자 지정 ch01-01-terminal-problem 승인 표지의 위치·크기로 왼쪽 공통 statement와 오른쪽 단일 장면 이미지를 배치한다. 본문은 무엇을 주고 / 무엇을 받을까. 제목·부제의 소개 문구를 반복하지 않는다."
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 2. AI의 입력과 출력

역할: INPUT_AI_OUTPUT

> AI에 넣는 자료와 요청이 Input이고, 작업을 거쳐 받는 결과물이 Output입니다.

화면 문구·요소: Input · 입력: 자료 + 요청 / AI · 에이전트: 맡긴 작업 수행 / Output · 출력: 원하는 결과물

시각: 입력 → AI → 출력의 가로 흐름. 입력 purple, AI brand, 결과 green. 문서와 로봇을 크게 배치한다.

슬라이드: 1장
근거: 사용자 2026-09-22 지시 및 무료 세미나의 AI 입력·출력, 출력 우선 설계, 작업 연결 설명. 고객 문의 예시는 이번 강의용으로 변경.

### 3. 출력부터 정하는 설계

역할: OUTPUT_FIRST

> 받고 싶은 결과의 내용과 형식을 정하면, 필요한 자료와 요청을 정할 수 있습니다.

화면 문구·요소: 원하는 출력: 고객 문의 유형표(유형 / 반복 질문 / 답변 근거). 필요한 입력: 고객 문의 원문 + 상품·배송·교환 정책. 요청: 문의 유형·반복 질문·답변 근거를 표로 정리해줘.

시각: 왼쪽에 완성 형태의 표, 오른쪽에 필요한 입력 자료와 요청. 설계 순서는 출력 결정 → 입력 도출이며 실행 흐름과 구별해 표시한다.

슬라이드: 1장
근거: 사용자 2026-09-22 지시 및 무료 세미나의 AI 입력·출력, 출력 우선 설계, 작업 연결 설명. 고객 문의 예시는 이번 강의용으로 변경.

### 4. 출력과 입력의 연결

역할: ARTIFACT_HANDOFF (세미나 보관 순차 실행 2장 구조 재사용)

> 앞 에이전트의 결과물을 받은 뒤, 다음 에이전트가 작업을 시작합니다.

화면: 위쪽 사람 ↔ Coordinator, 아래쪽 Worker A(문의 분류 · 완료) → 문의 유형표 → Worker B(FAQ 개선안 작성). 문의 유형표로 향하는 화살표는 Output, 문의 유형표에서 다음 워커로 향하는 화살표는 Input이다. 문서 한 장을 공유하며 복제본을 그리지 않는다.

조율: Worker A의 완료 보고 → Coordinator의 완료 확인 → Worker B 작업 배정. 하단 문서 연결은 결과 의존 관계이고 워커끼리 직접 실행을 지시하는 관계가 아니다.

하단: 코디네이터가 완료를 확인하고, 결과물을 넘겨 다음 작업을 배정합니다.

근거: 사용자 지정 세미나 보관본(무료 세미나 덱 `multi-agent-design.html`의 순차 2단계 장표) 두 번째 상태. 반영 후 보관본은 정리했다. 기존 고객 문의 → 문의 유형표 → FAQ 개선안 예시 유지.
슬라이드: 1장

### 5. 협업을 나누는 기준

역할: OPEN_TRIPTYCH 4관계 변형

> 파일이 만들어진 뒤 어디에 쓰이는지가 협업 구조를 정합니다.

화면 문구·요소:
```json
{
  "items": [
    [
      "앞 결과 전달",
      "다음 작업의 입력",
      "순차 전달 도식"
    ],
    [
      "작성·평가 분리",
      "서로 다른 담당이 검토",
      "되돌아오는 검토 도식"
    ],
    [
      "시안 중 선택",
      "같은 의뢰의 다른 결과",
      "분기 후 선택 도식"
    ],
    [
      "역할별 모두 활용",
      "각 채널에 맞춘 결과",
      "분기 후 각 결과 보존 도식"
    ]
  ],
  "note": "결과를 이어 쓸지, 검토할지, 골라 쓸지, 모두 쓸지에 따라 협업 방식이 달라집니다."
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 6. 판매 아이템 기획서

역할: SCENE_IMAGE

> 스마트스토어에서 팔 아이템과 실행 계획을 하나의 문서로 만듭니다.

화면 문구·요소:
```json
{
  "image": "pattern-1-sequential.png",
  "pattern": "순차 파이프라인",
  "color": "brand",
  "statement": "앞 결과를 받아\n다음 작업으로",
  "lines": [
    "차박용 접이식 미니 수납함 판매 아이템 기획서",
    "시장조사에서 후보 비교를 거쳐 기획서로"
  ],
  "link": "https://fastcampus-orca-course.vercel.app/project1-sidehustle-proposal/final/proposal-final.html",
  "linklabel": "판매 아이템 기획서 보기"
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 7. 클라이언트 제안서

역할: SCENE_IMAGE

> 작성한 제안과 견적을 다른 에이전트가 기준에 맞춰 평가합니다.

화면 문구·요소:
```json
{
  "image": "pattern-2-cross-check.png",
  "pattern": "교차 검증",
  "color": "purple",
  "statement": "작성과 평가를\n서로 다른 담당에게",
  "lines": [
    "무브펫 자동 순환 급수기 제안·견적서",
    "작성 → 평가 → 반려 사항 수정"
  ],
  "link": "https://fastcampus-orca-course.vercel.app/project2-ads-proposal/final/proposal-quote-final.html",
  "linklabel": "무브펫 제안·견적서 보기"
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 8. 프로모션 시안

역할: SCENE_IMAGE

> 같은 브랜드와 행사 조건을 주고 서로 다른 디자인을 받습니다.

화면 문구·요소:
```json
{
  "image": "pattern-3-parallel.png",
  "pattern": "병렬 실행",
  "color": "yellow",
  "statement": "같은 요청을 맡기고\n사람이 선택",
  "lines": [
    "무드온 블랙프라이데이 랜딩페이지",
    "같은 요청으로 두 시안 제작 후 비교·선택"
  ],
  "link": "https://fastcampus-orca-course.vercel.app/project3-blackfriday-landing/final/preview.html",
  "linklabel": "무드온 시안 두 개 보기"
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 9. 플랫폼별 콘텐츠

역할: SCENE_IMAGE

> 하나의 레시피를 채널마다 다른 역할의 콘텐츠로 확장합니다.

화면 문구·요소:
```json
{
  "image": "pattern-4-rnr.png",
  "pattern": "R&R 분배",
  "color": "green",
  "statement": "다른 역할로 나눠\n결과를 모두 활용",
  "lines": [
    "스트로베리 퐁당 케이크 콘텐츠 3종",
    "한 레시피에서 블로그·카드뉴스·스레드로"
  ],
  "link": "https://fastcampus-orca-course.vercel.app/project4-recipe-content/final/preview.html",
  "linklabel": "레시피 콘텐츠 3종 보기"
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 10. 선택과 활용의 차이

역할: TRANSITION_COMPARE

> 둘 다 동시에 만들지만 결과물을 사용하는 방식이 다릅니다.

화면 문구·요소:
```json
{
  "sides": [
    {
      "title": "병렬 실행",
      "color": "yellow",
      "root": "같은 랜딩페이지 요청",
      "leaves": [
        "시안 A",
        "시안 B"
      ],
      "result": "사람이 하나 선택"
    },
    {
      "title": "R&R 분배",
      "color": "green",
      "root": "하나의 레시피 소재",
      "leaves": [
        "블로그",
        "카드뉴스",
        "스레드"
      ],
      "result": "역할별 결과 모두 활용"
    }
  ]
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 11. 업무에 맞는 패턴

역할: CAUSE_ROWS

> 업무가 요구하는 관계를 확인하면 패턴을 고를 수 있습니다.

화면 문구·요소:
```json
{
  "rows": [
    [
      "앞 결과가 다음 작업에 필요한가?",
      "순차 파이프라인",
      "brand"
    ],
    [
      "완성본을 별도로 검사해야 하는가?",
      "교차 검증",
      "purple"
    ],
    [
      "같은 의뢰의 다른 안을 보고 싶은가?",
      "병렬 실행",
      "yellow"
    ],
    [
      "다른 채널의 결과가 모두 필요한가?",
      "R&R 분배",
      "green"
    ]
  ]
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

### 12. 기획팀 프로젝트

역할: SCENE_IMAGE

> 먼저 하나의 결과물을 순서대로 완성하는 구조를 만듭니다.

화면 문구·요소:
```json
{
  "image": "pattern-1-sequential.png",
  "statement": "시장조사에서\n판매 아이템 기획서까지",
  "lines": [
    "Part 5 · 기획팀",
    "입력과 결과가 이어지는 협업"
  ]
}
```

슬라이드: 1장
근거: Part 1 소개 7·8장 및 네 프로젝트 완성본

## 2026-09-22 무료 세미나 참조 범위

- 참조: `../fastcampus-orca-course/free-seminar/final/slides/multi-agent-design.html`의 4장 AI의 입력과 출력, 6~8장 입력·출력 사례와 형식 지정, 11장 업무를 나누는 기준.
- 개념은 유지하고 세미나의 매일커피·회의 안건 예시와 기계형 UI는 재사용하지 않는다. 새 예시는 고객 문의 유형표 → FAQ 개선안이다.
- 실행 순서(Input → AI → Output)와 사람이 설계하는 순서(원하는 Output 결정 → 필요한 Input 도출)를 구별한다. 기존 프로젝트 4개와 링크는 보존한다.

### 지정 표지 대조 기준

- `artifacts/part2/outputs/ch01-01-terminal-problem.html` 본문 좌측 3%, 폭 34%, 이미지 좌측 35%, 폭 65%, 본문 높이 100%. 표지 본문 padding 0.
- 공통 Pretendard, 본문 clamp(2rem,3.8vw,3.7rem), weight 850 / 강조 900, line-height 1.35, letter-spacing -.035em.
- 인물은 지정 표지의 갈색 머리·성인 비율·흰 얼굴과 흰 셔츠·검은 윤곽선·절제된 음영을 직접 참조한다. 지친 표정만 새 주제에 맞게 집중하는 표정으로 바꾼다.

### 최신 이미지 선택 — 여러 명 협업 장면

최종 표지는 `ch01-01-collaboration-patterns--cover-team-transparent.png`를 사용한다. terminal-problem 원본과 동일한 1536×1024(3:2) RGBA PNG이며 배경은 실제 투명이다. 남자 1명과 로봇 3명의 협업 장면을 좁고 높게 재배치하고, 타원형 책상 전체가 자연스럽게 끝나도록 생성했다. 이전 cover-team.png의 2:1 가로 구도와 불투명 사각 배경은 사용하지 않는다. 표지 CSS·문구·폰트·이미지 컨테이너 위치와 크기는 그대로다.
