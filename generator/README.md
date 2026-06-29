# Dashboard generator

`idium_gen.py` builds Home Assistant storage-mode Lovelace JSON for all Idium dashboards.

## Usage

```bash
# From repository root
./scripts/generate.sh

# Or directly
python3 generator/idium_gen.py
```

Output: `dist/ha_write_manifest.json` (12 files).

## Configuration

Copy `config/idium.example.json` → `config/idium.json`.

Environment variables:

| Variable | Default |
|----------|---------|
| `IDIUM_CONFIG` | `{repo}/config/idium.json` |
| `IDIUM_MANIFEST` | `{repo}/dist/ha_write_manifest.json` |

## Customization

| What | Where |
|------|-------|
| Owner name, alarm, key entities | `config/idium.json` |
| Room list, scenes, sidebar | `generator/idium_gen.py` |
| Design tokens (frozen v1.0) | `C` dict in `idium_gen.py` + `themes/` |

## Version

Generator version matches repository `VERSION` file (currently **1.0.0**).

Releasing a new version:

1. Bump `VERSION` in `idium_gen.py` and root `VERSION` file
2. Update `CHANGELOG.md`
3. Run `./scripts/generate.sh`
4. Tag `git tag v1.x.x`

## No third-party dependencies

Python 3.9+ standard library only (`json`, `pathlib`, `os`).
