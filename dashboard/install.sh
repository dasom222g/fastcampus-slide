#!/bin/sh
# 커밋 훅을 켠다. 저장소마다 한 번만 실행하면 된다.
set -e
cd "$(git rev-parse --show-toplevel)"

chmod +x dashboard/hooks/pre-commit dashboard/src/build.py
git config core.hooksPath dashboard/hooks

echo "설치 완료 — 이제 커밋할 때마다 대시보드가 갱신된다."
echo "  훅 위치   dashboard/hooks"
echo "  끄기      git config --unset core.hooksPath"
echo
python3 dashboard/src/build.py
