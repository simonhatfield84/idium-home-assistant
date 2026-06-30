# Deploying dashboards

The generator writes Home Assistant **storage-mode** Lovelace files — the same JSON that lives under `.storage/` in your config.

## Generate

```bash
./scripts/generate.sh
# → dist/ha_write_manifest.json
```

That manifest maps paths to file contents:

| File | What |
|------|------|
| `.storage/lovelace.lovelace` | Home |
| `.storage/lovelace.dashboard_*` | Room dashboards |
| `.storage/lovelace_dashboards` | Sidebar |
| `.storage/lovelace_resources` | Card JS URLs |

## Copy to HA

**File Editor / Studio Code Server** — open each key in the manifest, create/overwrite the matching file under `/config/.storage/`, paste the JSON value.

**SSH / Samba:**

```bash
./scripts/deploy.sh /path/to/homeassistant/config
```

Or copy by hand.

## Restart once

HA reads these at startup. Copy everything first, then **Settings → System → Restart** once. Hard-refresh clients after.

Don't restart between individual files — one batch, one restart.

## After deploy

1. **Settings → Dashboards → Resources** — Mushroom, card-mod, mini-graph should be there
2. Open Home, click around the nav pills
3. Profile theme → **idium_dark**
4. Fix any “Entity not found” in `config/idium.json`, regenerate, redeploy

## Updating

```bash
git pull
./scripts/generate.sh
./scripts/deploy.sh /config
# restart once
```

## Rollback

Back up `.storage/` before you overwrite. Restore the old files and restart if you need to undo.
