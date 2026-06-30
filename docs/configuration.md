# Configuration

Copy the example and edit it for your home:

```bash
cp config/idium.example.json config/idium.json
```

Override paths if you like:

| Variable | Purpose |
|----------|---------|
| `IDIUM_CONFIG` | Path to config JSON |
| `IDIUM_MANIFEST` | Where to write the generated manifest |

## `idium.json`

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

**`owner_name`** — shows up in the Home greeting (“Good morning, …”).

**`theme`** — `idium_dark` or `idium_light`.

**`entities`** — the main entities wired into a few shared cards. Everything else (rooms, scenes, nav) still lives in `generator/idium_gen.py` unless you edit it there.

| Key | Used for |
|-----|----------|
| `alarm` | Security cards |
| `whole_house_lights` | All lights off, home lighting tile |
| `weather` | Home weather card |
| `doors_status` | Door summary |
| `home_average_*` | Whole-home climate |
| `office_*` | Office dashboard |
| `living_room_lights` | Home living room tile |

## Rooms and scenes

The generator is built around my floor plan — multiple rooms, Hue scenes, office scripts. To make it yours:

1. Fix the keys in `config/idium.json` for the shared cards
2. Edit `generator/idium_gen.py` for rooms, nav, scenes:
   - `NAV` / `NAV_SECONDARY`
   - per-room `scene_grid(...)` calls
   - sidebar entries

I may pull more of that into JSON later ([ROADMAP.md](../ROADMAP.md)).

## Optional helpers

`packages/idium_helpers.yaml.example` has light groups, a doors template sensor, home average temp/humidity, and office scene tracking. Rename, edit every entity ID, then include via packages.

## Themes

After editing YAML in `themes/`: **Settings → Dashboards → Themes → Reload**. No restart needed for theme-only changes.

## Cache busting

The generator appends `?v100` (from the semver) to Lovelace resource URLs. Bump `VERSION` in the generator when you release, regenerate, redeploy `lovelace_resources`.
