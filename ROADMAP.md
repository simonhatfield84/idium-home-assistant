# Roadmap

Idium **v1.0.0 design is frozen**. The items below are planned for future semver releases without changing the established visual language unless noted.

## v1.1.x — Customization & portability

- [ ] Entity discovery helper script (suggest `config/idium.json` from HA API)
- [ ] Split generator constants into `generator/rooms/` modules
- [ ] Documented “minimal install” (themes only, no generator)
- [ ] Example `configuration.yaml` snippet in docs

## v1.2.x — Quality of life

- [ ] Per-room active scene tracking (Bedroom, Living Room)
- [ ] Motion cards with last-triggered timestamps
- [ ] Energy overview card (optional, off by default)
- [ ] Light theme parity audit

## v2.0.0 — Future (design review required)

- [ ] YAML-first dashboard config (reduce Python customization)
- [ ] Optional light/dynamic accent themes
- [ ] Tablet / wall-panel layout preset
- [ ] i18n for greeting and labels

## Non-goals

- Replacing Home Assistant sidebar or core UI
- Bundling Mushroom / card-mod (remain HACS dependencies)
- Alarm panel replacement (works with native / third-party alarm entities)

## How to influence the roadmap

Open a [Feature request](.github/ISSUE_TEMPLATE/feature_request.yml) issue. UI changes that affect v1.x aesthetics will be tagged **design-review**.
