#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 generator/idium_gen.py
echo "Manifest written to dist/ha_write_manifest.json"
