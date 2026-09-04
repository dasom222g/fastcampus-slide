# Orca 설치 전 준비물 스토리보드

**소스:** 채팅으로 받은 3장 구성 초안 + `edu-slide/source/ORCA_ORCHESTRATION_NOTES.md` 「1. Orca — Agent Development Environment」
**참고 덱:** `edu-slide/output/hermes-bot.html`
**출력 슬라이드:** `edu-slide/output/orca-install-prep.html`
**총 슬라이드:** 3장 (표지 1장 + 본문 2장)
**디자인 기준:** edu-slide 스킬 `assets/base-template.html` (다크 · 컬러 팔레트)

---

## 용어 규칙

| 이 덱에서 쓰는 말 | 원문 표기 | 쓰지 않는 말 |
|---|---|---|
| 클로드 코드 | `Claude Code` | Claude CLI, 클로드 CLI |
| 코덱스 | `Codex` | Codex CLI(화면 제목) |
| 오르카 | `Orca` | 에이전트 |
| 로그인 | `LOGIN COMPLETE`(상태 딱지) | 계정 연동, 인증 연결 |

- 제품명은 실제 CLI 이름과 맞도록 영문 원문을 크게 노출한다.
- `Orca`는 두 CLI를 대신 설치하거나 로그인하는 도구처럼 표현하지 않는다.

---

## 주제 도출

| 항목 | 내용 |
|---|---|
| 한 줄 주제 | Orca를 설치하기 전에 Claude Code와 Codex를 설치하고 각 CLI 로그인까지 완료해야 한다. |
| 청중 | AI 코딩 CLI를 사용해봤고 Orca 설치 실습을 처음 따라오는 개발자·AI 자동화 실무자 |
| 핵심 주장 1 | Orca 설치 전에 연결할 AI CLI를 먼저 준비한다. |
| 핵심 주장 2 | 이번 실습의 준비물은 Claude Code와 Codex 두 가지다. |
| 핵심 주장 3 | 두 CLI는 각각 로그인된 상태여야 Orca에서 연결할 수 있다. |

**버릴 내용**

- 각 CLI 설치 명령어 — 사용자가 정한 3장 범위가 준비물과 로그인 상태까지이므로 후속 실습 화면에서 다룬다.
- Orca의 ADE 정의와 오케스트레이션 기능 — 설치 전 준비물이라는 한 메시지에서 벗어난다.
- 버전 수치 — 화면에 노출할 필요가 없고 설치 시점에 따라 달라진다.
- METRIC 타입 — 소스에 이 덱에서 사용할 수치가 없다.

**색 배정**

| 대상 | 색 |
|---|---|
| Orca · 덱 기본 축 | teal |
| Claude Code 카드 | teal (로고 고유 주황은 유지) |
| Codex 카드 | blue-violet |
| 로그인 완료 상태 | green |
| 보조 라벨·설명 | gray |

---

## 슬라이드 구성

| # | 타입 | 제목 | 핵심 메시지 |
|---|---|---|---|
| 1 | TEXT | Orca 설치 전 준비물 | Orca를 설치하기 전에 연결할 AI CLI부터 준비한다. |
| 2 | CARD_GRID(2) | 준비물 두 가지 | 이번 실습에 필요한 CLI는 Claude Code와 Codex다. |
| 3 | CARD_GRID(2) | 로그인까지 완료 | 각 CLI에 로그인된 상태여야 Orca에서 연결할 수 있다. |

---

## 슬라이드 1 / 3 — Orca 설치 전 준비물

- **타입:** TEXT (대형 로고 표지)
- **핵심 메시지:** Orca를 설치하기 전에 연결할 AI CLI부터 준비한다.
- **근거:** 사용자 구성 초안 「1장: Orca 설치 전 준비물」 + 소스 「1. Orca — Agent Development Environment」 — “각 CLI의 설치와 계정 로그인은 별도로 필요하며”

**화면 요소**

| 요소 | 내용 |
|---|---|
| slide__label | Orca Setup · 설치 전 준비 |
| slide__title | Orca 설치 전 **준비물** |
| slide__sub | Orca를 설치하기 전에 연결할 CLI부터 준비한다 |
| 대형 로고 (teal) | `../images/orca-logo.svg` / Orca 로고 |
| 선언문 (teal) | `Orca보다 먼저` / `AI CLI부터 준비` |
| 축 라벨 (gray) | `CLAUDE CODE · CODEX` |

> `hermes-bot.html`의 큰 표지 프레임과 본문 높이를 참고하되, 별도 생성 이미지 없이 Orca 로고와 선언문을 화면 중앙에 가까이 붙인다.

**애니메이션 순서**

1. Orca 로고 fadeInUp
2. 선언문 fadeInUp
3. 축 라벨 fadeInUp

**발표 노트**
> Orca부터 바로 설치하기 전에 준비할 것이 있습니다. Orca가 실행할 AI 코딩 CLI를 먼저 설치해 두고, 각 CLI에서 로그인까지 끝낸 상태로 시작하겠습니다.

---

## 슬라이드 2 / 3 — 준비물 두 가지

- **타입:** CARD_GRID(2) — 좌우 대형 카드
- **핵심 메시지:** 이번 실습에 필요한 CLI는 Claude Code와 Codex다.
- **근거:** 사용자 구성 초안 「2장: 준비물 두 가지 — Claude Code, Codex」 + 소스 「1. Orca — Agent Development Environment」 — “Codex·Claude Code·Cursor CLI 같은 기존 AI 코딩 도구”

**화면 요소**

| 요소 | 내용 |
|---|---|
| slide__label | Prerequisites · 준비물 |
| slide__title | 준비물 **두 가지** |
| slide__sub | 이번 실습에서는 Claude Code와 Codex를 Orca에 연결한다 |
| 카드 1 (teal) | 딱지 `CLI 01` / 대형 `../images/claude-code-logo.png` / 제목 `Claude Code` |
| 카드 2 (blue-violet) | 딱지 `CLI 02` / 대형 `../images/codex-logo.svg` / 제목 `Codex` |

**애니메이션 순서**

1. Claude Code 카드 fadeInUp
2. Codex 카드 fadeInUp

**발표 노트**
> 준비물은 두 가지입니다. Claude Code와 Codex를 모두 설치해 주세요. 다음 화면에서 설치 여부보다 먼저 확인할 것은 각 CLI의 로그인 상태입니다.

---

## 슬라이드 3 / 3 — 로그인까지 완료

- **타입:** CARD_GRID(2) — 로그인 상태가 붙은 좌우 대형 카드
- **핵심 메시지:** 각 CLI에 로그인된 상태여야 Orca에서 연결할 수 있다.
- **근거:** 사용자 구성 초안 「3장: 로그인까지 완료 — 각 CLI에 로그인된 상태여야 연결됨」 + 소스 「1. Orca — Agent Development Environment」 — “각 CLI의 설치와 계정 로그인은 별도로 필요하며”

**화면 요소**

| 요소 | 내용 |
|---|---|
| slide__label | Account Login · 로그인 |
| slide__title | 로그인까지 **완료** |
| slide__sub | 각 CLI에 로그인된 상태여야 Orca에서 연결할 수 있다 |
| 상태 카드 1 (teal + green) | 대형 `../images/claude-code-logo.png` / 제목 `Claude Code` / 상태 딱지 `LOGIN COMPLETE` |
| 상태 카드 2 (blue-violet + green) | 대형 `../images/codex-logo.svg` / 제목 `Codex` / 상태 딱지 `LOGIN COMPLETE` |
| 대형 결론 (green) | `각 CLI 로그인 완료` / `Orca 연결 준비 완료` |

**애니메이션 순서**

1. Claude Code 로그인 카드 fadeInUp
2. Codex 로그인 카드 fadeInUp
3. 대형 결론 fadeInUp

**발표 노트**
> 설치만 되어 있으면 끝이 아닙니다. Claude Code와 Codex를 각각 한 번 실행해서 로그인을 마쳐 주세요. 두 CLI 모두 로그인된 상태여야 Orca에서 바로 연결해 사용할 수 있습니다.

---

## 조작 규칙

- 슬라이드 이동은 **좌우 화살표 버튼 · 하단 점 · 키보드 ← →/스페이스**로만 한다.
- 화면 아무 데나 클릭해서 넘기지 않는다.
- 마지막 슬라이드에서 다음 버튼, 첫 슬라이드에서 이전 버튼은 비활성 처리한다.
