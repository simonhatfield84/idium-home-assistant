# Idium Design System v1.0

Design tokens for Idium **v1.0.0** (frozen).

## Principles

1. **Restraint** — colour communicates state, not decoration  
2. **Typography first** — hierarchy through weight and size, not boxes  
3. **Calm motion** — 100–250ms transitions; no gratuitous animation  
4. **Mobile-native** — thumb reach, compact nav, minimal scroll  

## Colour

### Surfaces

| Token | Value | Usage |
|-------|-------|-------|
| Background | `#0B0D10` | Page |
| Surface | `rgba(255,255,255,0.035)` | Cards |
| Stroke | `rgba(255,255,255,0.06)` | Card border |
| Divider | `#2C3138` | Sliders, separators |

### Text

| Token | Hex | Usage |
|-------|-----|-------|
| Primary | `#F5F7FA` | Values, titles |
| Secondary | `#A3A8B1` | Labels |
| Disabled | `#6E737B` | Inactive icons, legends |

### Semantic accents

| Domain | Hex | Usage |
|--------|-----|-------|
| Active / Success | `#30D158` | Active scenes, nav pill, scene chips |
| Climate | `#5DA3FF` | Temperature icons, sparklines |
| Lighting | `#F5B14C` | Light sliders when on |
| Heating | `#FF8A3D` | Thermostat |
| Security | `#FF5A5A` | Alarm armed, open doors |
| Media | `#7C8CFF` | Spotify / media accents |

No gradients on cards. No drop shadows in v1.0 (flat translucent surfaces).

## Typography

```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', Inter, system-ui, sans-serif;
```

| Role | Weight | Size |
|------|--------|------|
| Hero value | 300 | 28px |
| Section label | 500 | 10–11px uppercase, 0.8px tracking |
| Body | 400–500 | 13–15px |
| Nav pill | 400–500 | 10–11px |

## Spacing

8px grid.

| Context | Padding |
|---------|---------|
| Page (mobile) | 20px horizontal |
| Page (desktop) | 28px horizontal |
| Office desktop | 12px horizontal |
| Card internal | 8–16px |

## Radius

| Element | Radius |
|---------|--------|
| Cards | 16px |
| Nav pills | 14px |
| Scene chips | 10px |

## Components

### Navigation

- **Primary row:** Home, Dining, Office (compact)
- **Secondary row:** Bedroom, Living Room (larger)
- **More row:** Kitchen, Security, Climate, Hall, Dressing

### Alarm

Grey when disarmed. When armed: red icon, red label, subtle red card tint.

### Climate

Large value + uppercase label + 36px sparkline with inline `24h` legend (7px, bottom-right).

### Scenes

Inactive: `rgba(255,255,255,0.04)`. Active: green glow `#30D158` at 24% opacity.

Office: manual light changes → **Custom** via automation (optional helpers package).

### Office layout

Desktop: no side icon rail. Lighting | Sound row. Halo independent from room filament group.

## Stack

| Layer | Package |
|-------|---------|
| Theme | `themes/idium_dark.yaml` |
| Cards | Mushroom |
| Graphs | mini-graph-card |
| CSS | card-mod |

## Light theme

`idium_light` mirrors tokens for light backgrounds. Primary accent blue `#4A8FE7`.
