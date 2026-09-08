---
상태: 최종 확정
산출물: artifacts/part2/outputs/ch01-02-what-is-orca.html
슬라이드: 5장
---

# Orca는 어떤 도구인가 — 최종 화면 기준 소스

사용자가 확정한 Codex 작업본을 정식 최종본으로 승격했다. 이전 Orca 초안과 orca2는 폐기했다.

## 슬라이드 1 — Orca의 정체

Part 2 · ch01-02 · Orca는 어떤 도구인가
Orca의 정체
Orca는 여러 에이전트가 일하는 작업 환경입니다.
여러 에이전트가각자 일하는 환경
비유하면 에이전트들의 작업장입니다.

## 슬라이드 2 — Orca 안에서 일하는 AI

Part 2 · ch01-02 · Orca는 어떤 도구인가
Orca 안에서 일하는 AI
새 모델을 사는 것이 아니라 이미 쓰는 에이전트를 연결합니다.
Orca
여러 에이전트를 한곳에 두고 소통하게 하는 작업 공간
에이전트 A
Claude Code
이미 쓰는 구독을 그대로 연결
에이전트 B
Codex
이미 쓰는 구독을 그대로 연결

## 슬라이드 3 — IDE와 ADE

Part 2 · ch01-02 · Orca는 어떤 도구인가
IDE와 ADE
직접 작성하는 환경에서 에이전트에게 맡기고 검토하는 환경으로 옮겨갑니다.
IDE
Integrated Development Environment
사람 중심 환경
파일 열기
→
작성
→
실행
→
저장
ADE
Agent Development Environment
에이전트 중심 환경
작업 생성
→
공간 생성
→
에이전트 실행
→
결과 검토

## 슬라이드 4 — Orca의 작업 단위

Orca는 워크트리 단위로 작업을 나눕니다.

- 워크트리
- 프로젝트 파일을 따로 꺼내 작업하는 폴더
- 에이전트는 이 워크트리 안에서 작업합니다.

설명 범위: Orca의 기본 작업 단위가 워크트리이며, 실제 프로젝트 파일을 두고 수정하는 작업 폴더라는 점까지.
배경 정확성: Git은 선택한 버전의 파일을 작업 폴더에 준비한다. 같은 저장소와 연결되어 있으므로 저장소 전체를 독립 복제한 clone과 동일시하지 않는다. 버전·브랜치·생성 명령은 다음 Git 파트에서 다룬다.
확인: https://git-scm.com/docs/git-worktree 의 DESCRIPTION 및 add 설명.

## 슬라이드 5 — 오케스트레이션까지

여러 에이전트에게 일을 나누고 결과를 모읍니다.

- 하나의 목표
- 에이전트 A · 에이전트 B · 에이전트 C
- 모인 결과
- 작업 배정 · 진행 확인 · 결과 취합

Orca에서 여러 에이전트의 일을 하나의 흐름으로 구성할 수 있음을 예고한다. 조율 담당자와 스킬의 내부 작동 방식은 이 장에서 설명하지 않는다. 설치와 실행 절차는 실습에서 다룬다.

## 확인 근거

- Orca 공식 제품 소개: https://www.onorca.dev/
- Git worktree 공식 문서: https://git-scm.com/docs/git-worktree
- Orca 공식 오케스트레이션 가이드: https://github.com/stablyai/orca/blob/main/skill-guides/orchestration.md
- 설치된 Orca CLI 가이드: `orca skills get orca-cli` (2026-09-08 확인).
