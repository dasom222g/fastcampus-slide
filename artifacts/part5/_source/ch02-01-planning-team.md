---
파트: part5
챕터: Chapter 2
클립: Ch02-01. 기획팀 구조와 업무 흐름
길이: 11분
슬라이드: 6장
산출물: artifacts/part5/outputs/ch02-01-planning-team.html
상태: 작성중
---

# 기획팀 구조와 업무 흐름

제작 목표: 사람은 사업 목표와 기준을 정하고 에이전트는 맡은 문서를 완성합니다.

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

## 화면 구성

1. 기획팀 구조와 업무 흐름: 사람이 기준을 정하고 에이전트가 문서를 만드는 표지. 왼쪽 문구·오른쪽 투명 배경 장면 이미지.
2. 판매 아이템 기획서: 완성할 문서의 선정·계획·점검 세 항목.
3. 사람의 결정: 사업 조건 → 업무 기준 → 에이전트의 입력.
4. 기획팀의 구조: 사람의 목표·기준을 Coordinator가 Worker A·B·C에게 배정하는 관계도.
5. 순차 작업과 산출물: Worker A의 시장 조사 노트 → Worker B의 아이템 후보 비교표 → Worker C의 판매 아이템 기획서. 각 산출물이 다음 워커의 입력으로 들어간다.
6. 코디네이터의 전달: Worker A가 저장한 시장 조사 노트를 Coordinator가 파일·필수 내용으로 확인하고 Worker B에게 넘긴다. 워커끼리 직접 소통하지 않는다.

4~6장의 도식은 노드·화살표의 좌표를 고정하고 등장만 opacity 페이드로 처리한다. 첫 프레임과 마지막 프레임의 위치가 같아야 하며, 위치가 흔들린다는 이유로 애니메이션을 끄지 않는다.

5장은 담당마다 산출물이 다르고 그 산출물이 다음 담당의 입력이 된다는 관계를 보여준다. 담당에서 자기 산출물로는 실선(Output), 산출물에서 다음 담당으로는 점선(Input)을 쓴다. 6장은 그 점선 구간을 펼쳐 문서 → 코디네이터 확인 → 다음 담당 입력으로 잇는다. 워커끼리 직접 주고받지 않는다는 것은 경로로만 보여주고 차단 표시는 넣지 않는다.
