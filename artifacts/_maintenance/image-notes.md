# 이미지 생성 기록

## artifacts/part1/_images/ch02-01-single-agent-limits/README.md

# 최종본 이미지

| 파일 | 사용 장 | 출처 |
|---|---|---|
| `human-directs-ai-executes.png` | 2장 하나로 되는 일 | 사용자 확정 codex V1 이미지. 사람이 요청하고 AI가 직접 실행하는 장면 |

표지와 나머지 장은 HTML 안의 SVG 도식이며, 공유 로고는 `/assets/`에서 불러온다.


## codex/_production/revisions/single-agent-02/image-prompt.md

Use case: style-transfer / illustration-story
Asset type: Korean lecture slide illustration.
Input 1 (A): exact character design, white bodies, brown-haired simple cartoon person, dark outlines and restrained shallow 2.5D shading.
Input 2 (C): role/composition reference. The human gives instructions using a brief; the one AI agent executes the work.
Create a scene combining A's style with C's assignment of roles. Exactly one human on the left side of the subject group and one white rounded robot on the right at a gray desk. The human holds a brief upright and points to its simple unlettered marks, instructing the robot. The robot alone operates an open laptop with its own hands on the keyboard; it looks toward the laptop and carries out the task. The person is not typing or writing the deliverable. Preserve the robot's white rounded head/body and black pill visor with one red horizontal light. Person has brown simple hair, white shirt and face, tiny black oval eyes. No realistic sculpted man, armored robot, separate eyes or antenna.
Composition: 1536x1024 landscape, subjects large in right 60%, left 35% clear dark negative space for HTML text. Dark #0d1117 background, gray desk/laptop, bright clearly visible white characters. Clean black contours and soft shallow cel shading as A. No letters, logos, captions, arrows, watermark.


## codex/_production/revisions/single-agent-02/scene-ledger.md

# 장면 원장
- 사람: 요청을 들고 옆자리 → 브리프를 가리키며 지시 → 에이전트에 작업을 맡김 → 키보드나 펜으로 결과물을 직접 제작하지 않음.
- 에이전트 한 명: 요청을 받음 → 노트북 키보드를 직접 조작 → 결과물을 제작 → 양손이 입력 장치에 닿고 시선은 노트북으로 향함.
- 브리프: 사람 손에 들린 요청 문서. 결과물과 구분.
- 결과: 노트북에서 에이전트가 만드는 상태. AI가 보조만 하는 장면으로 보이지 않아야 함.
- A의 스타일, C의 지시/실행 역할 구분을 결합. 다음 본문 장에 사용하고 표지는 별도의 SVG 관계도.

## 생성 후 검수
- 사람 1명, 봇 1명. 사람이 요청서를 들고 손가락으로 지시하고 봇의 손은 노트북 키보드에 위치함.
- A의 밝은 흰 몸체·갈색 머리·짙은 윤곽선과 C의 역할 배치를 유지함.
- 내장 imagegen 사용. 결과: part1/_images/ch02-01-single-agent-limits/human-directs-ai-executes.png. 프롬프트: 같은 폴더 image-prompt.md.


## codex/part2/_images/ch01-02-what-is-orca/agent-office-equipped-prompt.md

# 에이전트 작업실 이미지

방식: built-in image_gen으로 기존 공통 공간 이미지를 편집.

최종 파일: agent-office-equipped-v3.png

장면 검수: 사람 0명, 흰 에이전트 3명. 개별 모니터·파일, 공용 진행 보드, 메시지·자료 영역을 하나의 작업실 안에 배치. 회색 공간은 작업 환경을 이해시키는 시각적 비유이며 실제 Orca 화면을 재현한 것이 아니다.

프롬프트:

Edit this reference into a clearly recognizable shared AGENT WORK STUDIO, not merely three desks inside glass walls. Keep the EXACT existing clean outlined 2.5D illustration style and white rounded robot identity: black horizontal visor, red / blue-violet / cool-gray face bars. Exactly THREE robots, ZERO humans. Show a spacious furnished cutaway office interior with a clearly connected floor, tall solid rear wall, side walls, doorway, and a short ceiling beam; the front and roof are opened so the interior can be seen. The room must look like a usable working environment, not a glass display case. The neutral gray environment is the main subject and the three agents are its occupants. Communicate what the environment provides through concrete functional objects: (1) THREE clearly separate equipped workstations, each with a large upright monitor displaying simple terminal prompt bars and document/code lines, keyboard, laptop or desk surface, and a small personal folder/document tray, (2) ONE large shared wall-mounted task progress board behind the workstations with three columns of clearly separated task cards, some status dots and check marks, (3) a shared wall-mounted message/handoff area with simple message bubbles and document icons, plus a subtle shared cable/channel running between the three workstations to suggest connected communication. The agents are actively typing or reading at their own stations. Avoid posing robots merely in a row; arrange the three stations naturally within one room, two along the back wall and one closer to the open front, with walkable space between. No server racks, no clouds, no claims of automatic collaboration, no labels or legible text, no logos. Palette: dark #0d1117 surrounding canvas, mid-gray architectural surfaces bright enough to see, white robots, restrained red #fc1c49 and blue-violet accents and muted status colors. NO photorealistic people, no dark metal robots, no neon sci-fi spaceship. Framing: wide landscape 3:2, a large richly readable office cutaway occupying the RIGHT 75-80% of the frame and almost full image height; only the LEFT 20-25% should remain quiet dark for HTML overlay. Architecture, monitors, shared progress board and message area must all be clearly legible at slide size. Keep every workstation inside one single connected room. Make the environment substantially larger and better equipped than the reference.


## codex/part2/_images/ch01-02-what-is-orca/shared-environment-prompt.md

# 공통 작업 환경 이미지

방식: built-in image_gen · 기존 agent-office.png 편집.

검수 기준: 사람 0명, 기존 흰 봇 3명, 각자 책상·노트북, 세 봇 전체를 감싸는 하나의 연속된 회색 외곽 경계, 기존 2.5D 선화와 색상 유지.

최종 파일: agent-office-shared-v2.png

프롬프트:

Edit the provided reference image for a Korean educational slide. Preserve its exact clean 2.5D illustrated style: crisp dark outlines, gently shaded white rounded robots, black horizontal pill-shaped face visor, small luminous horizontal face bars, neutral gray desks and laptops, dark #0d1117 background. Remove the human completely, including the tablet, legs, and shadow. Keep exactly THREE white robot agents, each sitting at its own desk with laptop, with face bar accents red #fc1c49, blue-violet, and cool gray, as in the reference. Show all three desks INSIDE ONE shared enclosing work environment: a single neutral-gray softly outlined open-front cutaway workspace, one continuous floor platform and one continuous back/side boundary surrounding all three agents together, subtly translucent walls so nothing is obscured. The continuous outer enclosure must be unmistakable at a glance; no three individual cubicles, no separate boxes, no cage. Arrange desks in a compact staggered/isometric row, all within that one shared workspace, viewed from the same front-left elevated camera angle as the reference. Keep agents bright white, friendly and simple, not metallic or photorealistic. Place the entire shared workspace in the right 65% of a wide 3:2 image; the left 30-35% is quiet dark negative space for HTML text overlay. Leave a little margin around the entire outer enclosure so it is fully visible and not cropped. No people, no fourth robot, no text, no labels, no logos, no watermarks. A scene illustration, not a software screenshot.


## Orca 표지 v4 — 2026-09-08

- 생성: 내장 image_gen 도구, 참조 이미지 2개 사용.
- 기준: `artifacts/part2/_images/image--agent-office-shared-v2--2864b5de9f.png`의 로봇·배치·화풍.
- 환경 참조: `artifacts/part2/_images/ch01-02-what-is-orca--agent-office-equipped-v3.png`의 사무실·보드.
- 결과: `artifacts/part2/_images/ch01-02-what-is-orca--agent-office-v4.png`
- 검수 캡처: `artifacts/part2/_qa/orca-cover-after-1280.png`, `orca-cover-after-1920.png`.

프롬프트 핵심: 첫 번째 참조의 흰색 로봇 세 명과 정면으로 보이는 얼굴, 대각선 책상 배치, 단순한 검은 윤곽선과 부드러운 입체감을 유지한다. 두 번째 참조에서는 하나의 사무실임을 보여주는 벽·문·공용 진행 보드·메시지 보드만 가져온다. 노트북으로 일하는 로봇이 주인공이며 소파·과도한 가구·복잡한 케이블·사람을 넣지 않는다. 정사각형 중앙 구도, 짙은 #0d1117 배경, 그림 전체를 여백 안에 넣고 글자·로고·워터마크 없이 생성한다. 로봇 바이저는 빨강·보라·회청색으로 구분한다.


## part4 · ch03-02-solo-business-skills 표지 (미생성, 2026-09-19)

상태: 생성 보류. Higgsfield 크레딧 0, Codex image_gen 사용 한도 초과(2026-09-20 13:23 이후 가능). 현재 표지는 Part 3의 `ch01-01-what-is-git--version-history-transparent.png`를 재사용한다.

장면 원장
- 사람: 문서 여러 장이 꽂힌 트레이 앞 → 한 장을 뽑아 듦 → 에이전트에게 건넴.
- 에이전트: 옆자리 → 한 손을 내밀어 그 문서를 받음 → 다른 손은 노트북 위.
- 문서: 고른 한 장만 red 막대, 나머지는 회색. 글자 없음.
- 검수 기준: 사람 1명, 봇 1명, 고른 문서 1장만 강조, 배경 #0d1117, 글자·로고·화살표 없음.

참조 입력: `part1/_images/ch02-01-single-agent-limits--human-directs-ai-executes.png`(캐릭터·화풍), `part3/_images/ch01-01-what-is-git--version-history.png`(문서 트레이).

프롬프트:

Use the built-in image generation tool (image_gen) to create ONE illustration, then save the PNG to
artifacts/part4/_images/ch03-02-solo-business-skills--cover.png . Do not edit any other file. Do not write HTML.

Use case: style-transfer / illustration-story. Asset type: Korean lecture slide cover illustration.
Input 1 (A): exact character design and rendering style. Brown-haired simple cartoon person in a white long-sleeve top, white rounded robot with a black horizontal visor and a red face bar, clean dark outlines, restrained shallow 2.5D cel shading, gray desk.
Input 2 (B): reference for document cards standing in a gray desk tray with simple red unlettered bars.

Scene: choosing the right guide for the agent. Exactly ONE human on the left and ONE white robot on the right, at a gray desk. On the desk in front of the human stands a gray tray holding FOUR upright document cards. Three cards are muted gray with faint gray bars. The human has pulled ONE card out of the tray: it is white with simple red unlettered bars, and the human is handing it toward the robot with one hand while the other hand still rests on the tray. The robot reaches out with one hand to receive that card and looks at it; its other hand rests on an open gray laptop. The human looks friendly and confident. Only the chosen card is red-accented, so it clearly reads as "this one, out of several".

Composition: 1536x1024 landscape, subjects large and centered, whole desk visible, a little dark margin on every side. Background: flat dark #0d1117 that melts into a dark slide, no floor line, no vignette border, no frame. Bright clearly visible white characters, gray furniture. Colors limited to white, grays, brown hair, red #fc1c49 accents. No letters, no numbers, no logos, no captions, no arrows, no UI windows, no watermark.


## artifacts/part5/_source/ch04-04-quality-gate-image-prompts.md

# 3장 역할 대비 이미지 제작 기록

도구: 내장 image_gen, 두 개의 독립 생성 호출. CLI/API fallback 미사용. 원본은 `/Users/dasom/.codex/generated_images/01a0bf02-0b07-7bc2-ba12-fd24325389c0/`에 보존하고 프로젝트에 복사했다.

## 공통 프롬프트

Create a professional instructional slide illustration asset, landscape 3:2. No letters, no words, no labels, no arrows, no diagram, no logos. Isolated compact desk vignette on a perfectly flat solid #0d1117 background, generous empty margins, no floor horizon. Restrained high quality soft 3D editorial illustration, matte ceramic white and slate materials, crisp silhouettes, subtle shadows, no neon glow, no busy decoration. This is one of a coordinated pair for a Korean business course explaining creation versus verification. Character should be an approachable small robot agent with an opaque white rounded head and dark face visor, understated, not a human. The physical action and props must communicate the role instantly; occupy the central 80% with large readable props.

## 생성 담당 — 공통 프롬프트 뒤에 추가

CREATION ROLE: compact stocky white robot with red #fc1c49 shoulder and face accents seated at a low writing desk, actually writing on a large unfinished paper report with a red pencil in right hand. On its left a clearly separate upright open reference rulebook, which the robot consults while composing. Paper report has a few abstract gray horizontal marks and visible empty space to suggest work in progress. Reference book has simple bullet glyphs only. Three-quarter front view. Red pencil and in-progress writing are the unmistakable focal point. No magnifying glass, no tick marks, no approval seals. Make the robot body form and posture visibly that of a maker.

원본: `exec-aaf3d916-5e70-4edb-88ac-865632d3c1b0.png` → `artifacts/part5/_images/ch04-04-quality-gate--creation.png`

## 검증 담당 — 공통 프롬프트 뒤에 추가

VERIFICATION ROLE: taller white robot with a distinctly squarer head, yellow #f7c85a accents, standing at a compact examination desk. It is examining a finished green-tabbed report using a LARGE handheld magnifying glass in one hand while holding a separate inspection checklist in the other. The completed report has neatly filled abstract gray line marks. Checklist shows small empty square boxes and two restrained tick marks, no words. Three-quarter front view, composition same overall visual size as a writing-desk vignette. Magnifying glass held prominently OVER the finished report must be instantly legible. Yellow inspector silhouette and inspection tools contrast with a red seated writing robot; no pencil, no creation activity, no automatic conveyor belt, no external connections.

원본: `exec-0f5d2c7f-8596-46c7-b89a-bc6cae602081.png` → `artifacts/part5/_images/ch04-04-quality-gate--verification.png`

## 육안 확인

작성 장면에는 규칙책·연필·작성 중 문서, 검증 장면에는 돋보기·검사표·완성 문서가 식별된다. 두 역할의 도구·자세·색이 다르며 이미지에 한글 라벨이나 단계 연결이 없다. 라벨은 HTML로 표시한다.
