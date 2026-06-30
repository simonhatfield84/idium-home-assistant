# Design notes

Colours and spacing I used for v1.0.0. Handy if you're tweaking the generator or themes.

## Colours (dark theme)

### Surfaces

| | Value | Use |
|---|-------|-----|
| Background | `#0B0D10` | Page |
| Surface | `rgba(255,255,255,0.035)` | Cards |
| Stroke | `rgba(255,255,255,0.06)` | Borders |
| Divider | `#2C3138` | Sliders |

### Text

| | Hex |
|---|-----|
| Primary | `#F5F7FA` |
| Secondary | `#A3A8B1` |
| Muted | `#6E737B` |

### Accents

| | Hex | Use |
|---|-----|-----|
| Active | `#30D158` | Scenes, nav |
| Climate | `#5DA3FF` | Temp, graphs |
| Lighting | `#F5B14C` | Light sliders |
| Heating | `#FF8A3D` | Thermostat |
| Security | `#FF5A5A` | Alarm armed, open doors |
| Media | `#7C8CFF` | Spotify |

Flat cards — no gradients or drop shadows in v1.0.

## Type

```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', Inter, system-ui, sans-serif;
```

Section labels are small caps (~10–11px). Hero numbers are light weight, ~28px.

## Spacing

Rough 8px grid. Mobile pages ~20px horizontal padding; office desktop a bit tighter (12px).

## Radius

Cards 16px, nav pills 14px, scene chips 10px.

## Layout bits

- **Nav:** two rows of room pills + a “More” row (Kitchen, Security, Climate, etc.)
- **Alarm:** grey when off, red tint when armed
- **Climate:** big number + 36px sparkline, tiny `24h` label
- **Scenes:** green glow when active
- **Office:** no side icon rail on desktop; Halo separate from room lights

## Stack

| | Package |
|---|---------|
| Theme | `themes/idium_dark.yaml` |
| Cards | Mushroom |
| Graphs | mini-graph-card |
| CSS | card-mod |

Light theme (`idium_light`) is the same idea on a light background; accent blue `#4A8FE7`.
