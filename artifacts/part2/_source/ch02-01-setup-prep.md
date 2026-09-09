---
파트: part2 — Orca 설치 및 기본 사용
챕터: Chapter 2. Orca 설치와 첫 실행
클립: Ch02-01. 설치 전 준비물과 환경 체크
길이: 5분
슬라이드: 3장                      # 표지 없이 본문 3장 — 2026-09-09 사용자 지시로 표지를 다시 걷어내고 09-07 구성(3장)으로 되돌렸다.
산출물: artifacts/part2/outputs/ch02-01-setup-prep.html
상태: 최종 확정
유형: 참고 노트 (구성안이 아니라 원본 자료. 구성은 _storyboard/ 참조)
---

# Orca Orchestration 이해하기

Orca의 `/orchestration` 스킬이 여러 에이전트를 어떻게 조율하는지 이해하기 위한 개인 학습 노트다. 명령어·플래그의 정확한 사양은 `orca skills get orchestration`이 기준이며, 이 문서는 개념과 흐름만 다룬다. (git 미추적)

## 1. Orca — Agent Development Environment

Orca는 새로운 AI 모델이나 코딩 agent가 아니라, Codex·Claude Code·Cursor CLI 같은 기존 AI 코딩 도구를 독립된 작업 공간에서 실행하고 한 화면에서 관리하는 오픈소스 **ADE(Agent Development Environment)**다. 각 CLI의 설치와 계정 로그인은 별도로 필요하며, Orca는 현재 작업에 맞는 디렉터리에서 이들을 실행해 터미널·상태·변경 사항을 관리한다.

IDE가 사람이 직접 코드를 작성하는 환경이라면, ADE는 여러 agent에게 작업을 맡기고 결과를 검토하는 환경이다.

```text
IDE: 파일 열기 → 코드 작성 → 실행·테스트 → 커밋
ADE: 작업 생성 → worktree 생성 → agent 실행 → diff 검토 → 커밋·PR
```

Orca의 기본 기능은 여러 작업과 agent를 나란히 실행·비교하는 것이다. 설치만으로 agent들이 자동 협업하는 것은 아니며, 작업 분해·메시지 전달·완료 추적까지 맡기려면 별도의 orchestration 기능을 사용한다.

## 2. 기존 도구의 한계를 깬 방식

기존 AI 코딩 도구는 기본적으로 **에디터 하나에서 agent 하나와 작업하는 방식**을 전제로 한다. 여러 agent를 함께 쓰려면 개발자가 터미널·세션·에디터를 늘어놓고, 각 agent가 어느 작업을 맡았는지 직접 관리해야 한다.

> **기존 도구:** 에디터 하나 + agent 하나  
> **Orca:** 여러 agent의 동시 실행이 기본값

Orca는 이 전제를 바꿔 여러 코딩 agent를 한곳에서 병렬 운영하는 작업 공간을 제공한다.

```text
동시 실행 → 작업 분배 → 진행 확인 → 결과 비교
```

업계에서 말하는 "10배 빠르게 일하는 개발자"도 한 agent의 능력이 10배가 된다는 뜻보다, 독립적인 작업에 여러 agent를 동시에 투입해 처리량을 높인다는 비유에 가깝다. 실제 효율은 병렬로 나눌 수 있는 작업의 수와 결과를 검토·통합하는 비용에 따라 달라진다.

## 3. Orca의 작업 단위 — worktree

Orca는 실제 **Git worktree**를 기본 작업 단위로 사용한다. Git worktree는 같은 저장소의 여러 브랜치를 서로 다른 디렉터리에 동시에 열어 주므로, 각 agent가 별도의 브랜치와 파일에서 작업할 수 있다. 여러 agent가 동시에 실행돼도 변경 사항이 섞이거나 같은 파일을 직접 덮어쓸 위험을 줄인다.

```text
저장소
├── worktree A: 브랜치 A + harness/agent A
├── worktree B: 브랜치 B + harness/agent B
└── worktree C: 브랜치 C + harness/agent C
```

Orca의 worktree는 Git 디렉터리만 뜻하지 않는다. 해당 작업의 브랜치와 파일, agent·일반 터미널, 편집기·브라우저 탭, 기준 브랜치와의 diff, 커밋·PR 상태를 함께 묶어 관리하는 작업 공간이다. 서로 다른 일을 병렬로 맡길 수도 있고, 같은 문제를 여러 worktree에서 풀게 한 뒤 결과를 비교할 수도 있다. 작업이 끝나면 변경 사항을 커밋하거나, 필요 없는 worktree와 브랜치를 제거한다.

## 4. 병렬 실행의 두 방식

worktree가 분리되어 있으므로 여러 AI agent를 안전하게 병렬 실행할 수 있다. 활용 방식은 **서로 다른 작업을 나누는 분업**과 **같은 문제의 결과를 비교하는 경쟁 실행** 두 가지다.

### 서로 다른 작업을 나눠 맡긴다

```text
Codex       → 로그인 API 수정
Claude Code → 테스트 코드 작성
Cursor CLI  → 문서 업데이트
```

작업 간 의존성이 적고 수정할 파일이 겹치지 않을수록 효과적이다. 한 agent가 작업하는 동안 다른 agent가 별도의 구현·테스트·문서 작업을 진행한다.

### 같은 문제를 여러 agent에게 맡긴다

```text
worktree A → Codex
worktree B → Claude Code
worktree C → Cursor CLI
```

각 worktree를 같은 기준 브랜치에서 시작하고 동일한 요청을 전달한 뒤, 테스트 결과·변경 범위·코드 구조를 비교해 가장 나은 결과를 선택한다. 해결 방법이 명확하지 않은 버그나 설계 선택지가 여러 개인 리팩터링에 유용하다.

## 5. 세 계층 — harness, agent, Orca

harness는 개별 agent의 실행 환경을 관리하고, Orca는 여러 agent가 협업할 수 있도록 전체 작업 환경을 운영한다. 이 문서에서는 셋을 다음처럼 구분한다.

| 용어 | 정의 | 예시 |
|---|---|---|
| **Harness** | 개별 agent를 실행하고 필요한 도구·파일·세션을 관리하는 환경 | 필요한 도구와 작업 파일이 갖춰진 개인 책상 |
| **Agent** | harness 안에서 역할과 목표를 받아 실제 작업을 수행하는 실행 인스턴스 | 책상에서 맡은 일을 수행하는 작업자 |
| **Orca** | 여러 harness와 agent를 역할별로 배치·호출하고 협업 과정과 작업 상태를 관리하는 운영 레이어 | 여러 작업자와 책상을 조율하는 운영실 |

구조는 `Orca → 여러 개의 (harness → agent)`로 이해하면 된다. harness는 개별 agent의 실행 기반이고, Orca는 이 실행 단위들을 조율하는 운영 레이어다. 하나의 harness에서 역할이 다른 여러 agent를 실행할 수 있고, 같은 역할도 서로 다른 harness에 배정할 수 있다. 일반적으로 말하는 "Claude agent"나 "Codex agent"는 어떤 harness에서 실행되는 agent인지를 기준으로 부르는 축약 표현이다.

## 6. Orchestration의 두 역할 — coordinator와 worker

Orca orchestration에 참여하는 agent는 **coordinator**와 **worker** 두 역할로 구분된다. 같은 Claude/Codex라도 어느 터미널에서 어떤 명령을 받았느냐에 따라 역할이 정해진다.

| 역할 | 누구 | 하는 일 | 쓰는 명령 |
|---|---|---|---|
| **Coordinator** | `/orchestration`을 받은 에이전트(보통 사람이 대화 중인 터미널) | 일을 쪼개 Task로 만들고, worker를 띄우고, 보고를 기다리며 질문에 답하고, 끝난 worker를 정리한다. **스스로 일을 하지 않는다** | `run-create`, `task-create`, `worker-start`, `check --wait`, `reply`, `worker-release` |
| **Worker** | coordinator가 띄운 터미널 안의 에이전트 | 받은 Task 하나만 수행하고, 막히면 묻고, 끝나면 정확히 한 번 보고한 뒤 멈춘다 | `ask`, `heartbeat`, `worker_done`(`send --type worker_done`), `escalation` |

둘을 잇는 것이 **preamble**이다. coordinator가 worker를 띄울 때 Orca가 Task spec 앞에 자동으로 붙이는 "생명주기 지시문"으로, worker에게 자기 `task_id`·`dispatch_id`, 보고 방법, 끝나면 멈추라는 규칙을 알려준다. worker가 `worker_done`을 보낼 수 있는 권한은 이 preamble에서 나온다. 터미널 히스토리에 남은 옛 preamble은 효력이 없다.

coordinator는 동시에 worker가 될 수 없고, worker는 다른 worker를 띄우지 않는다. 계층이 필요하면 coordinator가 Task 간 의존성(`--deps`)으로 표현한다.

## 7. 네 가지 객체 — Run, Task, Dispatch, Worker terminal

| 객체 | 비유 | 실체 |
|---|---|---|
| **Run** | 칸반 보드 (UI 없음) | 터미널·세션·프로세스가 **아니다**. Orca 내부 DB의 이름공간으로, 한 번의 조율 작업에서 오간 메시지와 Task 상태가 이 이름으로 분류된다. 만들어도 화면에 아무것도 생기지 않는다. 스케줄링도 하지 않는다 |
| **Task** | 보드의 티켓 (Ready 열, 담당자 없음) | "무엇을 할지" 적힌 spec. 상태는 `pending → ready → dispatched → completed / failed / blocked`. `--deps`로 선행 Task를 걸면 선행이 끝날 때까지 `pending` |
| **Dispatch** | 티켓에 담당자를 붙여 In Progress로 옮긴 기록 | Task 1개를 터미널 1개에 붙인 **시도**. 한 Task에 재시도가 있으면 Dispatch가 여러 개. 생명주기 권한(누가 `worker_done`을 보낼 수 있나, 누가 터미널을 정리하나)은 Run이 아니라 **Dispatch**에 있다 |
| **Worker terminal** | 직원의 책상 | 에이전트 TUI가 떠 있는 터미널. Dispatch가 붙어 있는 동안만 worker이고, 붙어 있지 않으면 그냥 터미널이다. 터미널 handle은 주소일 뿐 신원이 아니다 |

Run ⊃ Task ⊃ Dispatch → terminal 순서로 포함된다.

실제 배치는 이렇다. coordinator와 worker는 **각각 별개의 터미널·프로세스**이고, 서로의 화면을 보지 못한다. 대화는 오직 Run(메시지함)을 통해서만 오간다.

```text
워크트리
├── 터미널 A: coordinator 에이전트 (사람이 대화 중인 창)
├── 터미널 B: worker 1 에이전트        ← coordinator가 띄움, 독립 프로세스
└── 터미널 C: worker 2 에이전트        ← coordinator가 띄움, 독립 프로세스

Run = A·B·C의 Task와 메시지가 속하는 이름공간·메시지함 (UI 없음, `task-list`·`check`로 열람)
```

UI에서는 B·C가 A와 같은 워크트리의 탭으로 묶여 보이므로 "메인 에이전트 안에서 돈다"고 느끼기 쉽지만, 안이 아니라 옆에서 돈다. Run id는 "어느 메시지함인지", Dispatch id는 "어느 배정인지"를 말하며 둘은 다른 것이다.

## 8. 실행 시 내부에서 일어나는 일

```text
사람 ─ "/orchestration <할 일>" ─▶ Coordinator
                                     │
  ① run-create ───────────────────── Run 생성 (요청 1건 = Run 1개)
  ② task-create × N ──────────────── Task N개 생성 (spec만 있고 아직 Dispatch 없음, 상태 ready)
  ③ worker-start × N ─────────────── Task마다 터미널 확보 → 에이전트 기동
                                     → preamble + spec 주입 → Dispatch 생성 (상태 dispatched)
  ④ check --wait ──────────────────── Run 메시지함에서 question / heartbeat / escalation / worker_done 대기
       │
       ├─ question  ──▶ reply로 답 ──▶ 계속 대기
       ├─ heartbeat ──▶ 살아있음 신호, ack만
       ├─ escalation ▶ coordinator 개입 필요 (사람에게 올리거나 직접 결정)
       └─ worker_done ▶ ⑤ 결과 확인
                        ⑥ worker-release (정리) 또는 같은 터미널에 다음 Task 재사용
  ⑦ 모든 Dispatch가 settled 되면 종료

Worker (자기 터미널)
  preamble 읽기 → spec 수행 → 막히면 ask → 끝나면 worker_done(outcome, files) → 멈춤
```

중요한 성질:

- **Orca는 스케줄러가 아니다.** 몇 개로 쪼갤지, 어느 터미널에 붙일지, 언제 끝난 것으로 볼지는 전부 coordinator가 정한다. Orca는 (a) 메시지를 배달·보관하고, (b) Task/Dispatch 상태를 기록하고, (c) worker에게 preamble을 주입할 뿐이다.
- **`worker_done`은 정확히 한 번, 자기 터미널에서.** `--outcome succeeded|failed`를 명시해야 하며, 실패를 본문 글로만 적으면 Orca는 성공으로 기록한다.
- **대기는 "모든 Dispatch가 끝날 때까지"**지 횟수가 아니다. 하나 끝났다고 다음 worker를 띄우는 게 아니라, 독립 Task는 전부 먼저 띄우고 한꺼번에 기다린다.
- **끝난 worker는 반드시 처리한다.** 재사용(`worker-start --terminal`), 유지(`worker-retain`, 사람이 요청한 경우만), 해제(`worker-release`) 중 하나. 출력은 해제 후에도 `worker-read`로 읽을 수 있다.
- **메시지는 ack해야 사라진다.** 읽고 ack하지 않은 메시지는 다음 `check`에서 다시 배달된다.

## 9. 메시지 종류

| type | 방향 | 의미 |
|---|---|---|
| `question` (`ask`) | worker → coordinator | 막혀서 답이 필요. 옵션을 줄 수 있고, 답 올 때까지 worker는 대기 |
| `reply` | coordinator → worker | `question`에 대한 답 |
| `heartbeat` | worker → coordinator | 긴 작업 중 생존 신호. preamble이 요구할 때만 |
| `worker_done` | worker → coordinator | 최종 보고. outcome·수정 파일 포함 |
| `escalation` | worker → coordinator | 자기 권한 밖 — coordinator가 개입해야 함 |
| `gate` (`gate-create`/`gate-resolve`) | coordinator 내부 | Task DAG 진행 여부를 사람/coordinator가 결정하는 관문. worker의 질문 답변용이 아님 |

## 10. Orchestration이 아닌 것 — 풀 핸드오프

"이 일 다른 에이전트한테 넘겨줘(hand off)"는 orchestration이 아니라 **소유권 이전**이다. 넘긴 쪽은 더 이상 지켜보지 않으므로 Run/Task/Dispatch를 만들지 않고, `terminal create` + `terminal send`로 프롬프트만 전달한다. 사용자가 "감독해", "기다렸다 결과 알려줘", "여러 개 병렬로 돌려", "DAG로" 같은 말을 했을 때만 orchestration을 쓴다.

## 11. Automation — 예약 실행

Orchestration이 "일을 어떻게 나눠 시키는가"라면, **Automation은 "언제 시작하는가"**를 정하는 별개 기능이다. 등록해둔 프롬프트 하나를 정해진 시각에 자동으로 실행한다.

```text
스케줄 도달
  → Orca가 지정한 provider(claude·codex 등) 세션을 worktree에 띄움
  → 등록해둔 프롬프트 텍스트를 그 세션에 입력
  → 에이전트가 사람 없이 실행
  → 결과는 그 worktree에 남음
```

사람이 터미널에 프롬프트를 붙여넣는 것과 같은 일이 정해진 시각에 일어나는 것이다. 시작된 뒤 그 안에서 Run·Task·Dispatch가 만들어지는지는 프롬프트가 무엇을 지시하느냐에 달렸고, Automation 자체는 관여하지 않는다.

성질:

- **프롬프트는 고정 텍스트다.** 실행 시점에 값이 바뀌지 않으므로, 매번 다른 입력으로 돌리려면 등록한 프롬프트를 수정해야 한다.
- **실행 중에 사람에게 물을 수 없다.** 사람의 확인이 필요한 지점이 있는 작업은 거기서 멈추거나 에이전트가 임의로 판단한다.
- **worktree 모드**가 결과 위치를 정한다. 기존 worktree를 재사용하면 한곳에 쌓이고, 실행마다 새로 만들면 매번 분리된다.
- 스케줄은 프리셋(시간·일·주 단위), cron, RRULE로 지정한다.
