# Configuration

Idium reads optional settings from `config/idium.json` (copy from `config/idium.example.json`).

Environment overrides:

| Variable | Purpose |
|----------|---------|
| `IDIUM_CONFIG` | Path to config JSON |
| `IDIUM_MANIFEST` | Output path for generated manifest |

## Config file reference

```json
{
  "owner_name": "Home",
  "theme": "idium_dark",
  "entities": {
    "alarm": "alarm_control_panel.alarm",
    "whole_house_lights": "light.all_lights",
    "weather": "weather.forecast_home",
    "doors_status": "sensor.doors_status",
    "home_average_temperature": "sensor.home_average_temperature",
    "home_average_humidity": "sensor.home_average_humidity",
    "office_all_lights": "light.office_all_lights",
    "office_halo": "light.office_panel_light_controller",
    "office_room_lights": "light.office_room_lights",
    "office_media_player": "media_player.office_speaker",
    "office_active_scene": "input_select.office_active_scene",
    "living_room_lights": "light.living_room"
  }
}
```

### `owner_name`

Used in the Home greeting: “Good morning, {owner_name}”.

### `theme`

Lovelace theme key applied to all generated views. Use `idium_dark` or `idium_light`.

### `entities`

Subset of entities wired into configurable cards. The generator still contains a **reference room/scene map** — for full customization you will edit `generator/idium_gen.py` (see below).

| Key | Used for |
|-----|----------|
| `alarm` | Security cards, armed styling |
| `whole_house_lights` | All Lights Off action, Home lighting |
| `weather` | Home weather hero card |
| `doors_status` | Aggregated door summary sensor |
| `home_average_*` | Whole-home climate block |
| `office_*` | Office dashboard lighting, media, scenes |
| `living_room_lights` | Home dashboard living room tile |

## Customizing rooms and scenes

The generator ships with a **reference home** layout (multiple rooms, Hue scenes, office scripts). To adapt:

1. Map your entities in `config/idium.json` for top-level cards
2. Edit room definitions in `generator/idium_gen.py`:
   - `NAV` / `NAV_SECONDARY` — navigation targets
   - `SCENE_LABELS`, per-room `scene_grid(...)` calls
   - `sidebar` registry — sidebar visibility

Future releases will externalize room configs (see [ROADMAP.md](../ROADMAP.md)).

## Optional helpers package

`packages/idium_helpers.yaml.example` provides:

- Light **groups** (living ceiling, dining, office room vs halo)
- **Doors status** template sensor
- **Home average** temperature/humidity templates
- **Office scene tracking** (`input_select`, scripts, Custom automation)

Rename to `idium_helpers.yaml` and adjust every entity ID before use.

## Themes

Themes live in `themes/`. After editing:

- **Settings → Dashboards → Themes → Reload themes**
- No restart required for theme-only changes

## Resources cache busting

The generator sets Lovelace resource URLs with `?v100` (from semver). Increment `VERSION` in `generator/idium_gen.py` when releasing; regenerate and redeploy `lovelace_resources`.
