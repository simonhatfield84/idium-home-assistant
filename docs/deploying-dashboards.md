# Deploying dashboards

Idium generates Home Assistant **storage-mode** Lovelace files written to `.storage/` in your config directory.

## Generate manifest

```bash
./scripts/generate.sh
# Creates dist/ha_write_manifest.json
```

The manifest maps relative paths to JSON content:

| File | Purpose |
|------|---------|
| `.storage/lovelace.lovelace` | Home overview |
| `.storage/lovelace.dashboard_*` | Room dashboards |
| `.storage/lovelace_dashboards` | Sidebar registry |
| `.storage/lovelace_resources` | Mushroom / card-mod / mini-graph URLs |

## Deploy methods

### File Editor / Studio Code Server

1. Open each key in `dist/ha_write_manifest.json`
2. Create or overwrite the corresponding file under `/config/.storage/`
3. Paste the JSON **value** (pretty-printed string content)

### SSH / Samba

```bash
./scripts/deploy.sh /path/to/homeassistant/config
```

Or copy files manually from the manifest.

### Programmatic (API / MCP)

Write each manifest entry to HA config via your automation tool, then restart once.

## Important: one restart

Home Assistant loads `.storage` Lovelace configs at startup. After deploying dashboard files:

1. Run **Settings → System → Restart** once
2. Wait for HA to return (30–60 seconds)
3. Hard-refresh all clients

Do **not** restart between individual file copies.

## After deploy

1. Confirm resources: **Settings → Dashboards → Resources** — Mushroom, card-mod, mini-graph present
2. Open **Home** dashboard — verify navigation pills and cards
3. Set profile theme to **idium_dark**
4. Fix “Entity not found” by updating `config/idium.json` and regenerating

## Updating Idium

```bash
git pull
./scripts/generate.sh
./scripts/deploy.sh /config
# Restart HA once
```

Bump cache: change `VERSION` in generator before release so browsers reload frontend modules.

## Rollback

Home Assistant backs up `.storage` on some install methods. Keep a snapshot before deploying. To rollback, restore previous `.storage/lovelace.*` files and restart once.
