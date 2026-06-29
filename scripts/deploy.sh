#!/usr/bin/env bash
# Deploy Idium dashboard manifest to Home Assistant.
#
# Requires one of:
#   - Home Assistant MCP / File editor / SSH access to /config
#   - Vibecode Agent API or compatible file-write endpoint
#
# Usage:
#   ./scripts/deploy.sh /path/to/ha/config
#   HA_CONFIG=/config ./scripts/deploy.sh
#
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="${ROOT}/dist/ha_write_manifest.json"
TARGET="${1:-${HA_CONFIG:-}}"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Run ./scripts/generate.sh first." >&2
  exit 1
fi

if [[ -z "$TARGET" ]]; then
  cat <<EOF
No deploy target specified.

Copy files manually from dist/ha_write_manifest.json into your Home Assistant
config/.storage/ directory, then restart Home Assistant once.

See docs/deploying-dashboards.md for full instructions.
EOF
  exit 0
fi

python3 <<PY
import json, shutil
from pathlib import Path

manifest = json.loads(Path("$MANIFEST").read_text())
target = Path("$TARGET")
for rel, content in manifest.items():
    dest = target / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content if isinstance(content, str) else json.dumps(content, indent=2))
    print("wrote", dest)
print(f"Deployed {len(manifest)} files. Restart Home Assistant once to load dashboards.")
PY
