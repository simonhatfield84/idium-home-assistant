# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-29

First public release of **Idium Home Assistant**. Design frozen for this major version.

### Added

- **Design system** — `idium_dark` and `idium_light` themes
- **Dashboard generator** — `generator/idium_gen.py` producing 12 Lovelace storage files
- **Home dashboard** — greeting, weather, security row, all-lights-off action, climate, lighting, media, motion
- **Room dashboards** — Bedroom, Living Room, Dining, Kitchen, Office, Hall, Dressing, Climate
- **Security dashboard** — alarm, doors, motion sensors
- **Office landscape layout** — scenes, independent Halo lighting, Spotify now-playing, sound section
- **Navigation** — two-row primary pills; secondary “More” row (Kitchen, Security, Climate, Hall, Dressing)
- **Optional helpers package** — light groups, door status template sensor, office scene → Custom automation
- **Configuration** — `config/idium.example.json` for owner name, theme, and key entity IDs
- **Documentation** — installation, configuration, deployment, design system, contribution guides
- **HACS metadata** — theme installation via HACS
- **Branding assets** — SVG logo, mark, and banner
- **CI** — generator syntax validation workflow

### Design characteristics (v1.0.0)

- Background `#0B0D10`; subtle translucent card surfaces with hairline borders
- Green (`#30D158`) active states for scenes and navigation
- Red alarm styling when armed
- Inline `24h` climate sparkline legend
- Office desktop: no icon rail, tighter padding
- Mushroom + mini-graph-card + card-mod stack

### Notes

- Entity IDs in the generator reflect a reference home; customize via `config/idium.json` and edit the generator for full room/scene mapping.
- Deploying `.storage` dashboard files requires **one** Home Assistant restart.

[1.0.0]: https://github.com/simonhatfield/idium-home-assistant/releases/tag/v1.0.0
