# Dashboard generator

`idium_gen.py` builds the Lovelace JSON for all my dashboards.

```bash
# from repo root
./scripts/generate.sh

# or
python3 generator/idium_gen.py
```

Writes `dist/ha_write_manifest.json` (12 files).

## Config

`config/idium.json` — owner name, theme, main entity IDs. See [docs/configuration.md](../docs/configuration.md).

| Variable | Default |
|----------|---------|
| `IDIUM_CONFIG` | `{repo}/config/idium.json` |
| `IDIUM_MANIFEST` | `{repo}/dist/ha_write_manifest.json` |

## Where to edit what

| | File |
|---|------|
| Shared entities, greeting | `config/idium.json` |
| Rooms, scenes, nav | `generator/idium_gen.py` |
| Colours | `C` dict in `idium_gen.py` + `themes/` |

Version matches the root `VERSION` file. Bump both when you tag a release.

Python 3.9+, stdlib only.
