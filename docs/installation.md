# Installation

This guide installs Idium Home Assistant on a standard Home Assistant OS or Container setup.

## Requirements

| Requirement | Minimum |
|-------------|---------|
| Home Assistant | 2024.2+ |
| Python (for generator) | 3.9+ |
| HACS | Recommended |

### Required HACS frontend modules

Install before deploying dashboards:

1. **Mushroom Cards** — `piitaya/lovelace-mushroom`
2. **mini-graph-card** — `kalkih/mini-graph-card`
3. **card-mod** — `thomasloven/lovelace-card-mod`

### Home Assistant integrations

- **Recorder** — required for 24-hour climate sparklines
- **History** — recommended (enabled by default with recorder)

## Option A — Themes only (HACS)

1. Add Idium Home Assistant as a custom HACS repository (category: **Theme**)
2. Install and reload themes
3. Set your user profile theme to **idium_dark**

You keep your existing dashboards; only the theme changes.

## Option B — Full Idium dashboards

### Step 1 — Clone or download

```bash
git clone https://github.com/simonhatfield/idium-home-assistant.git
cd idium-home-assistant
```

### Step 2 — Install themes

**HACS:** as Option A.

**Manual:**

```bash
cp themes/*.yaml /config/themes/
# Settings → Dashboards → Themes → Reload themes
```

### Step 3 — Configure

```bash
cp config/idium.example.json config/idium.json
```

Edit `owner_name`, `theme`, and `entities` to match your installation.

### Step 4 — Generate

```bash
./scripts/generate.sh
```

### Step 5 — Deploy

See [deploying-dashboards.md](deploying-dashboards.md).

### Step 6 — Optional helpers

```bash
cp packages/idium_helpers.yaml.example packages/idium_helpers.yaml
```

Customize entity IDs, then ensure `configuration.yaml` includes:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

### Step 7 — Restart once

After copying `.storage` dashboard files and/or new packages:

1. **Settings → System → Restart Home Assistant**
2. Hard-refresh browsers (`Cmd+Shift+R` / force-quit mobile app)

## Verification checklist

- [ ] Profile theme is **idium_dark**
- [ ] Mushroom cards render (not “Custom element doesn't exist”)
- [ ] Home dashboard loads at `/lovelace/default_view`
- [ ] Climate graphs show lines (recorder running)
- [ ] No widespread “Entity not found” (customize config)

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Dashboard unchanged after deploy | Restart HA once; hard-refresh browser |
| Mushroom cards missing | Install Mushroom via HACS; check `lovelace_resources` |
| Graphs spin forever | Enable recorder; wait for history |
| Wrong entity names | Edit `config/idium.json` and/or generator entity map |

Next: [Configuration](configuration.md)
