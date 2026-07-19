#!/usr/bin/env bash
set -euo pipefail

DESTINATION_ROOT="${1:-${CODEX_HOME:-$HOME/.codex}/skills}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILL_NAME="civil-thesis-body-writing"
DESTINATION="$DESTINATION_ROOT/$SKILL_NAME"

mkdir -p "$DESTINATION_ROOT"

if [ -e "$DESTINATION" ]; then
  BACKUP="$DESTINATION.bak-$(date +%Y%m%d-%H%M%S)"
  mv "$DESTINATION" "$BACKUP"
  echo "Existing skill backed up to: $BACKUP"
fi

cp -R "$SKILL_ROOT" "$DESTINATION"

echo "Installed $SKILL_NAME to: $DESTINATION"
echo "Restart Codex to load the skill."
