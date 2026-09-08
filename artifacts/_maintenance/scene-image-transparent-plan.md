# SCENE_IMAGE 투명 PNG·템플릿 1번 반응형 수정

2026-09-08 사용자 최신 정정: 75% 고정 대신 기존 템플릿 1번의 규칙을 그대로 사용하며 템플릿 파일은 수정하지 않는다. 슬라이드 문구·순서·대본 의미는 유지한다.

- 원본의 검정 배경과 잘린 피사체를 실제 알파 채널이 있는 PNG로 재생성한다.
- 인물·로봇·책상은 캔버스 가장자리에서 끊기지 않고 전체가 보인다.
- 장면 묶음은 width:min(100%,92rem), 열 비율 1:1.65, 간격 clamp(1.5rem,3vw,3rem), 이미지 높이 min(78cqh,34rem), 중앙 정렬. 문장과 그림은 별도 열에 배치한다.
- object-fit: contain, 마스크·검정 박스·overflow 클리핑 없음.
- 그림은 partN/_images에 평면 저장. 원본과 실패 후보 보존.
- 2133×1200 / 1280×800에서 11개 장면을 검수한다.

- artifacts/part1/outputs/ch02-01-single-agent-limits.html · 2번 · 하나로 되는 일
- codex/part3/outputs/ch01-01-what-is-git.html · 2번 · Git의 역할
- codex/part3/outputs/ch01-01-what-is-git.html · 6번 · 필요한 만큼만
- codex/part3/outputs/ch01-02-repo-and-flow.html · 4번 · 골라두는 이유
- codex/part3/outputs/ch01-03-branch-vs-worktree.html · 3번 · 한 폴더의 한계
- codex/part3/outputs/ch01-03-branch-vs-worktree.html · 4번 · 폴더를 하나 더
- codex-v2/part3/outputs/ch01-01-what-is-git.html · 2번 · 이름 대신 기록
- codex-v2/part3/outputs/ch01-02-repo-and-flow.html · 3번 · 이번에 남길 변경
- codex-v2/part3/outputs/ch01-03-branch-vs-worktree.html · 1번 · 두 가지 수정안
- codex-v3/part3/outputs/ch01-01-what-is-git.html · 3번 · Git이 남기는 것
- codex-v3/part3/outputs/ch01-03-branch-vs-worktree.html · 4번 · 공간을 추가할 때
