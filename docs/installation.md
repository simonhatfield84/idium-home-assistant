# Installation

How I set this up on Home Assistant OS. Container installs work the same — paths are just `/config` instead of whatever yours is.

## Before you start

| | |
|---|---|
| Home Assistant | 2024.2+ |
| Python (for the generator) | 3.9+ |
| HACS | handy for the cards and themes |

Install these via HACS:

1. [Mushroom Cards](https://github.com/piitaya/lovelace-mushroom)
2. [mini-graph-card](https://github.com/kalkih/mini-graph-card)
3. [card-mod](https://github.com/thomasloven/lovelace-card-mod)

Turn on **Recorder** if you want the climate sparklines to show data.

## Themes only

1. HACS → add `https://github.com/simonhatfield84/idium-home-assistant` as a **Theme** repo
2. Install, reload themes
3. Profile → **idium_dark**

Your existing dashboards stay as they are.

## Full dashboards

```bash
git clone https://github.com/simonhatfield84/idium-home-assistant.git
cd idium-home-assistant
cp config/idium.example.json config/idium.json
```

Edit `idium.json` for your entities, then:

```bash
./scripts/generate.sh
```

Deploy — [deploying-dashboards.md](deploying-dashboards.md).

Optional: copy `packages/idium_helpers.yaml.example` → `idium_helpers.yaml`, fix entity IDs, add packages to `configuration.yaml`.

**Restart Home Assistant once** after writing `.storage` files or adding packages. Hard-refresh the browser after that.

## Quick check

- [ ] Theme is **idium_dark**
- [ ] Mushroom cards load (no “Custom element doesn't exist”)
- [ ] Home opens at `/lovelace/default_view`
- [ ] Climate graphs draw lines (give recorder a little time)
- [ ] No wall of “Entity not found” (you still need to map your IDs)

## When something's wrong

| Symptom | Try |
|---------|-----|
| Dashboard looks unchanged | Restart HA once, hard-refresh |
| Mushroom missing | Install via HACS, check lovelace resources |
| Graphs empty | Recorder on, wait for history |
| Wrong entities | `config/idium.json` and/or edit the generator |

Next: [Configuration](configuration.md)
