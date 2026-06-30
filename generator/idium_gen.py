#!/usr/bin/env python3
"""
Idium Home Assistant — dashboard generator.

See https://github.com/simonhatfield84/idium-home-assistant for documentation.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

VERSION = "1.0.0"
REPO_ROOT = Path(__file__).resolve().parents[1]


def _deep_merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def load_config() -> dict:
    """Load optional config/idium.json. See config/idium.example.json."""
    defaults = {
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
            "office_media_player": "media_player.office_speaker",
            "office_active_scene": "input_select.office_active_scene",
            "living_room_lights": "light.living_room",
        },
    }
    config_path = Path(os.environ.get("IDIUM_CONFIG", REPO_ROOT / "config" / "idium.json"))
    if config_path.is_file():
        with open(config_path, encoding="utf-8") as fh:
            return _deep_merge(defaults, json.load(fh))
    return defaults


CFG = load_config()

THEME = CFG["theme"]
OWNER_NAME = CFG["owner_name"]
E = CFG["entities"]
ALARM = E["alarm"]
OFFICE_ALL_LIGHTS = E["office_all_lights"]
OFFICE_HALO = E["office_halo"]
OFFICE_ROOM_LIGHTS = E.get("office_room_lights", "light.office_room_lights")
RESOURCE_TAG = f"v{VERSION.replace('.', '')}"


# ─── Semantic colour domains ────────────────────────────────────────────────
C = {
    "bg": "#0B0D10",
    "surface": "rgba(255, 255, 255, 0.035)",
    "surface_solid": "#13161B",
    "surface_elev": "rgba(255, 255, 255, 0.05)",
    "stroke": "rgba(255, 255, 255, 0.06)",
    "divider": "#2C3138",
    "text": "#F5F7FA",
    "text_sec": "#A3A8B1",
    "text_dis": "#6E737B",
    "climate": "#5DA3FF",
    "lighting": "#F5B14C",
    "heating": "#FF8A3D",
    "security": "#FF5A5A",
    "success": "#30D158",
    "active": "#30D158",
    "active_glow": "rgba(48, 209, 88, 0.24)",
    "media": "#7C8CFF",
    "shadow": "none",
}

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', Inter, system-ui, sans-serif"
PAD_MOBILE = "20px"
PAD_DESKTOP = "28px"

# Mobile nav — compact two rows, no horizontal scroll
NAV = [
    ("Home", "/lovelace/default_view", "mdi:home-outline"),
    ("Bedroom", "/dashboard-bedroom/bedroom", "mdi:bed-outline"),
    ("Living Room", "/dashboard-living-room/living-room", "mdi:sofa-outline"),
    ("Dining Room", "/dashboard-dining/dining-room", "mdi:silverware-fork-knife"),
    ("Office", "/dashboard-office/office", "mdi:monitor"),
]

NAV_SECONDARY = [
    ("Kitchen", "/dashboard-kitchen/kitchen", "mdi:stove"),
    ("Security", "/dashboard-home/home", "mdi:shield-outline"),
    ("Climate", "/dashboard-temperatures/temperatures", "mdi:thermometer-lines"),
    ("Hall", "/dashboard-hall-landing/hall-and-landing", "mdi:door-open"),
    ("Dressing", "/dashboard-dressing-room/dressing-room", "mdi:hanger"),
]


OFFICE_SCENES = [
    ("office_scene_working", "Working", "Working", "mdi:laptop"),
    ("office_scene_natural_light", "Natural", "Natural", "mdi:white-balance-sunny"),
    ("office_scene_concentrate", "Focus", "Focus", "mdi:brain"),
    ("office_scene_relax", "Relax", "Relax", "mdi:leaf"),
    ("office_scene_energise", "Energy", "Energy", "mdi:lightning-bolt-outline"),
    ("office_scene_nightlight", "Night", "Night", "mdi:weather-night"),
]

SCENE_LABELS = {
    "scene.master_bedroom_master_bedroom_bedtime": "Bedtime",
    "scene.master_bedroom_master_bedroom_nightlight": "Nightlight",
    "scene.master_bedroom_master_bedroom_relax": "Relax",
    "scene.master_bedroom_master_bedroom_read": "Read",
    "scene.master_bedroom_master_bedroom_reading": "Reading",
    "scene.master_bedroom_master_bedroom_energise": "Energise",
    "scene.master_bedroom_master_bedroom_concentrate": "Concentrate",
    "scene.master_bedroom_master_bedroom_chilled_custom": "Chill",
    "scene.bathroom_bathroom_nightlight": "Nightlight",
    "scene.living_room_living_room_relax": "Relax",
    "scene.living_room_living_room_watching_tv": "Watching TV",
    "scene.living_room_living_room_bright": "Bright",
    "scene.living_room_living_room_dimmed": "Dimmed",
    "scene.living_room_living_room_read": "Read",
    "scene.living_room_living_room_working": "Working",
    "scene.living_room_living_room_bright_chill": "Chill",
    "scene.living_room_living_room_nightlight": "Nightlight",
    "scene.dressing_room_dressing_room_read": "Read",
    "scene.dressing_room_dressing_room_relax": "Relax",
    "scene.dressing_room_dressing_room_dimmed": "Dimmed",
    "scene.dressing_room_dressing_room_nightlight": "Nightlight",
    "scene.dressing_room_dressing_room_rest": "Rest",
    "scene.dining_dining_relax": "Relax",
    "scene.dining_dining_read": "Read",
    "scene.dining_dining_energise": "Energise",
    "scene.dining_dining_nightlight": "Nightlight",
    "scene.dining_dining_chilled": "Chill",
    "scene.dining_dining_concentrate": "Concentrate",
    "scene.kitchen_kitchen_bright": "Bright",
    "scene.kitchen_kitchen_nightlight": "Nightlight",
    "scene.kitchen_kitchen_relax": "Relax",
    "scene.kitchen_kitchen_read": "Read",
    "scene.kitchen_kitchen_dimmed": "Dimmed",
    "scene.kitchen_kitchen_energise": "Energise",
    "scene.kitchen_kitchen_concentrate": "Concentrate",
    "scene.kitchen_kitchen_kitchen_chill": "Chill",
    "scene.hallway_hallway_nightlight": "Hall Night",
    "scene.landing_landing_nightlight": "Landing Night",
    "scene.hallway_hallway_bright": "Hall Bright",
    "scene.landing_landing_read": "Landing Read",
    "scene.entrance_zone_nightlight": "Entrance",
    "scene.porch_porch_bright": "Porch",
}

SCENE_ICONS = {
    "Nightlight": "mdi:weather-night",
    "Hall Night": "mdi:weather-night",
    "Landing Night": "mdi:weather-night",
    "Bedtime": "mdi:bed-outline",
    "Read": "mdi:book-open-variant",
    "Reading": "mdi:book-open-variant",
    "Landing Read": "mdi:book-open-variant",
    "Working": "mdi:laptop",
    "Focus": "mdi:brain",
    "Concentrate": "mdi:brain",
    "Relax": "mdi:leaf",
    "Rest": "mdi:leaf",
    "Energy": "mdi:lightning-bolt-outline",
    "Energise": "mdi:lightning-bolt-outline",
    "Chill": "mdi:snowflake",
    "Bright": "mdi:white-balance-sunny",
    "Hall Bright": "mdi:white-balance-sunny",
    "Dimmed": "mdi:brightness-6",
    "Watching TV": "mdi:television",
    "Natural": "mdi:white-balance-sunny",
    "Night": "mdi:weather-night",
    "Entrance": "mdi:door-open",
    "Porch": "mdi:outdoor-lamp",
    "Bedside": "mdi:lamp",
    "Artwork": "mdi:image-outline",
    "Chilled": "mdi:snowflake",
}


def storage_dashboard(key, config):
    return {"version": 1, "minor_version": 1, "key": key, "data": {"config": config}}


def vis(entity):
    return [{"condition": "state", "entity": entity, "state_not": ["unavailable", "unknown"]}]


def card_surface(extra=""):
    return {
        "style": f"""
ha-card {{
  background: {C['surface']};
  border: 1px solid {C['stroke']};
  box-shadow: none;
  border-radius: 16px;
  transition: background 150ms ease;
  font-family: {FONT};
  {extra}
}}
"""
    }


MOD_TRANSPARENT = {"style": "ha-card { background: transparent; border: none; box-shadow: none; margin: 0; padding: 0; }"}

MOD_TYPO_VALUE = {
    "style": f"""
mushroom-state-info$: |
  .primary {{
    font-family: {FONT};
    font-weight: 300;
    font-size: 26px;
    letter-spacing: 0.2px;
    line-height: 1.35;
    color: {C['text']};
  }}
  .secondary {{
    font-family: {FONT};
    font-weight: 400;
    font-size: 11px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    line-height: 1.4;
    color: {C['text_sec']};
    margin-top: 2px;
  }}
"""
}

MOD_TYPO_LABEL = {
    "style": f"""
mushroom-state-info$: |
  .primary {{
    font-family: {FONT};
    font-weight: 500;
    font-size: 14px;
    letter-spacing: 0.15px;
    line-height: 1.35;
    color: {C['text']};
  }}
  .secondary {{
    font-family: {FONT};
    font-weight: 400;
    font-size: 11px;
    letter-spacing: 0.4px;
    line-height: 1.4;
    color: {C['text_sec']};
  }}
"""
}

MOD_TYPO_OFFICE = {
    "style": f"""
mushroom-state-info$: |
  .primary {{
    font-family: {FONT};
    font-weight: 500;
    font-size: 13px;
    letter-spacing: 0.2px;
    line-height: 1.35;
    color: {C['text']};
  }}
  .secondary {{
    font-family: {FONT};
    font-weight: 400;
    font-size: 10px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    line-height: 1.4;
    color: {C['text_sec']};
  }}
"""
}


def section_label(text):
    return {
        "type": "custom:mushroom-template-card",
        "primary": text,
        "secondary": "",
        "icon": "mdi:minus",
        "layout": "horizontal",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 12px 2px 6px; margin: 20px 0 8px; }}
mushroom-shape-icon$ {{ display: none; }}
mushroom-state-info$: |
  .primary {{ font-family: {FONT}; font-weight: 500; font-size: 11px; letter-spacing: 0.8px; text-transform: uppercase; color: {C['text_dis']}; white-space: nowrap; }}
  .secondary {{ display: none; }}
"""
        },
    }


def sparkline(entity, color=None):
    color = color or C["climate"]
    card = {
        "type": "custom:mini-graph-card",
        "entities": [{"entity": entity, "color": color, "show_fill": False}],
        "hours_to_show": 24,
        "points_per_hour": 1,
        "line_width": 1.5,
        "height": 32,
        "update_interval": 300,
        "animate": True,
        "smoothing": True,
        "show": {
            "name": False, "icon": False, "state": False,
            "legend": False, "labels": False, "extremas": False, "fill": False,
        },
        "card_mod": {
            "style": f"""
ha-card {{
  background: transparent;
  border: none;
  box-shadow: none;
  border-radius: 0;
  height: 36px;
  margin: 0;
  position: relative;
}}
.card-content {{ padding: 0 !important; }}
ha-card::after {{
  content: '24h';
  position: absolute;
  right: 0;
  bottom: 0;
  font-family: {FONT};
  font-size: 7px;
  font-weight: 400;
  letter-spacing: 0.45px;
  text-transform: uppercase;
  color: {C['text_dis']};
  opacity: 0.65;
  line-height: 1;
  pointer-events: none;
}}
"""
        },
    }
    if entity:
        card["visibility"] = vis(entity)
    return card


def sensor_card(entity, label, unit="", icon="mdi:thermometer", domain_color="climate"):
    color = C.get(domain_color, C["climate"])
    primary = f"{{{{ states('{entity}') | float(0) | round(1) }}}}{unit}" if unit else f"{{{{ states('{entity}') }}}}"
    card = {
        "type": "custom:mushroom-template-card",
        "entity": entity,
        "primary": primary,
        "secondary": label,
        "icon": icon,
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 0; }}
mushroom-shape-icon$: {{ --icon-color: {color} !important; opacity: 0.85; }}
""" + MOD_TYPO_VALUE["style"]
        },
    }
    card["visibility"] = vis(entity)
    return card


def environment_card(temp_entity, hum_entity=None, location_label="Whole Home"):
    cards = [sensor_card(temp_entity, location_label, "°", "mdi:thermometer-outline", "climate")]
    cards.append(sparkline(temp_entity))
    if hum_entity:
        cards.append(sensor_card(hum_entity, location_label, "%", "mdi:water-percent", "climate"))
        cards.append(sparkline(hum_entity))
    return {
        "type": "vertical-stack",
        "cards": cards,
        "card_mod": {
            "style": f"""
ha-card {{
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 8px 0 4px;
}}
"""
        },
    }


def light_card(entity, name=None, color_control=False):
    card = {
        "type": "custom:mushroom-light-card",
        "entity": entity,
        "layout": "horizontal",
        "fill_container": True,
        "use_light_color": True,
        "show_brightness_control": True,
        "show_color_control": color_control,
        "collapsible_controls": True,
        "icon": "mdi:lightbulb-outline",
        "card_mod": {
            "style": f"""
ha-card {{ background: {C['surface']}; border: 1px solid {C['stroke']}; box-shadow: none; border-radius: 16px; font-family: {FONT}; width: 100%; }}
mushroom-state-info$: |
  .primary {{ font-weight: 500; font-size: 14px; letter-spacing: 0.15px; color: {C['text']}; white-space: nowrap; }}
  .secondary {{ font-size: 11px; letter-spacing: 0.3px; color: {C['text_sec']}; }}
mushroom-light-brightness-control$ mushroom-slider$: |
  .slider {{ height: 2px !important; border-radius: 1px; }}
  .slider-track {{ height: 2px !important; background: {C['divider']} !important; }}
  .slider-track-active {{ background: {C['lighting']} !important; }}
"""
        },
    }
    if name:
        card["name"] = name
    card["visibility"] = vis(entity)
    return card


def scene_icon(label):
    return SCENE_ICONS.get(label, "mdi:palette-outline")


def scene_card_scene(entity, label=None, active_entity=None, active_value=None):
    label = label or SCENE_LABELS.get(entity, "Scene")
    icon = scene_icon(label)
    inactive = f"""
ha-card {{
  background: rgba(255,255,255,0.04);
  border: none;
  box-shadow: none;
  border-radius: 10px;
  min-height: 28px;
  padding: 0;
  transition: all 150ms ease;
}}
mushroom-shape-icon$: {{ --icon-color: {C['text_dis']} !important; --icon-size: 18px; }}
mushroom-state-info$: |
  .primary {{ font-family: {FONT}; font-weight: 400; font-size: 11px; letter-spacing: 0.2px; color: {C['text_sec']}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .secondary {{ display: none; }}
"""
    active = f"""
ha-card {{
  background: {C['active_glow']};
  border: none;
  box-shadow: 0 0 14px rgba(48,209,88,0.14);
  border-radius: 10px;
  min-height: 28px;
  transition: all 150ms ease;
}}
mushroom-shape-icon$ {{ --icon-color: {C['active']} !important; --icon-size: 18px; filter: drop-shadow(0 0 5px rgba(48,209,88,0.45)); }}
.primary {{ color: {C['text']}; font-weight: 500; }}
"""
    style = inactive
    if active_entity and active_value:
        style = f"{{% if is_state('{active_entity}', '{active_value}') %}}{active}{{% else %}}{inactive}{{% endif %}}"
    return {
        "type": "custom:mushroom-template-card",
        "primary": label,
        "secondary": "",
        "icon": icon,
        "layout": "vertical",
        "icon_color": "grey",
        "tap_action": {"action": "call-service", "service": "scene.turn_on", "target": {"entity_id": entity}},
        "card_mod": {"style": style},
    }


def scene_card_script(script_id, label, active_option, icon=None, select_entity="input_select.office_active_scene"):
    icon = icon or scene_icon(label)
    active_bg = C["active_glow"]
    active_color = C["active"]
    return {
        "type": "custom:mushroom-template-card",
        "entity": select_entity,
        "primary": label,
        "secondary": "{% if is_state('" + select_entity + "', '" + active_option + "') %}Active{% else %}{% endif %}",
        "icon": icon,
        "layout": "vertical",
        "icon_color": "grey",
        "tap_action": {
            "action": "call-service",
            "service": "script.turn_on",
            "target": {"entity_id": f"script.{script_id}"},
        },
        "card_mod": {
            "style": f"""
ha-card {{
  background: rgba(255,255,255,0.04);
  border: none;
  box-shadow: none;
  border-radius: 10px;
  min-height: 28px;
  transition: all 150ms ease;
}}
{{% if is_state('{select_entity}', '{active_option}') %}}
  ha-card {{ background: {active_bg} !important; box-shadow: 0 0 18px rgba(48,209,88,0.18) !important; }}
  mushroom-shape-icon$ {{ --icon-color: {active_color} !important; --icon-size: 18px; filter: drop-shadow(0 0 6px rgba(48,209,88,0.55)); }}
  .primary {{ color: {C['text']} !important; font-weight: 500 !important; font-size: 11px !important; }}
  .secondary {{ color: {active_color} !important; font-size: 9px !important; text-transform: uppercase; letter-spacing: 0.5px; }}
{{% else %}}
  mushroom-shape-icon$ {{ --icon-color: {C['text_dis']} !important; --icon-size: 18px; }}
  .primary {{ color: {C['text_sec']}; font-weight: 400; font-size: 11px; letter-spacing: 0.2px; }}
  .secondary {{ display: none; }}
{{% endif %}}
"""
        },
    }


def scene_card_home(script_id, label, active_option, icon):
    return scene_card_script(script_id, label, active_option, icon, "input_select.home_active_scene")


def scene_grid(entities, columns=2):
    """Grid layout — 2 cols on mobile, avoids horizontal squeeze/truncation."""
    return {
        "type": "grid",
        "square": False,
        "columns": columns,
        "cards": [scene_card_scene(e) for e in entities],
        "card_mod": MOD_TRANSPARENT,
    }


def responsive_stack(*cards):
    """Side-by-side on desktop, stacked full-width on mobile."""
    return {
        "type": "horizontal-stack",
        "card_mod": {
            "style": """
@media (max-width: 900px) {
  #root { display: flex !important; flex-direction: column !important; }
  #root > * { width: 100% !important; min-width: 0 !important; }
  ha-card { width: 100% !important; }
}
"""
        },
        "cards": list(cards),
    }


MOD_DESKTOP_ONLY = {
    "style": """
@media (max-width: 900px) {
  :host { display: none !important; width: 0 !important; height: 0 !important; overflow: hidden !important; margin: 0 !important; padding: 0 !important; }
}
"""
}


MOD_PAGE_CONTENT = {
    "style": f"""
:host {{ background: {C['bg']} !important; }}
ha-card {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  margin: 0 !important;
}}
.card-content {{
  background: {C['bg']} !important;
  padding: 0 !important;
}}
"""
}


MOD_SUBTLE = {
    "style": f"""
ha-card {{
  background: {C['surface']};
  border: 1px solid {C['stroke']};
  box-shadow: none;
  border-radius: 14px;
  font-family: {FONT};
}}
"""
}


MOD_SHELL = {
    "style": f"""
:host {{
  background: {C['bg']} !important;
  box-sizing: border-box !important;
  padding: 8px {PAD_MOBILE} 20px {PAD_MOBILE} !important;
  display: block !important;
}}
@media (min-width: 901px) {{
  :host {{ padding: 12px {PAD_DESKTOP} 28px {PAD_DESKTOP} !important; display: flex !important; }}
  #root {{ display: flex !important; flex: 1; min-width: 0; }}
}}
@media (max-width: 900px) {{
  #root {{ display: block !important; }}
}}
ha-card {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}}
"""
}


MOD_SHELL_OFFICE = {
    "style": f"""
:host {{
  background: {C['bg']} !important;
  box-sizing: border-box !important;
  padding: 8px {PAD_MOBILE} 20px {PAD_MOBILE} !important;
  display: block !important;
}}
@media (min-width: 901px) {{
  :host {{ padding: 4px 12px 16px 12px !important; }}
}}
ha-card {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}}
"""
}


def shell_padding_mod():
    """Deprecated — padding lives on MOD_SHELL :host."""
    return MOD_SHELL


def spacer(px=16):
    return {
        "type": "custom:mushroom-template-card",
        "primary": "",
        "icon": "mdi:blank",
        "layout": "horizontal",
        "card_mod": {"style": f"ha-card {{ background: transparent; border: none; box-shadow: none; height: {px}px; min-height: {px}px; padding: 0; margin: 0; }} mushroom-state-info$ {{ display: none; }} mushroom-shape-icon$ {{ display: none; }}"},
    }


def security_card(entity, name, icon="mdi:motion-sensor-outline", subtitle="Motion sensor"):
    return {
        "type": "custom:mushroom-template-card",
        "entity": entity,
        "primary": name,
        "secondary": "{% set dc = state_attr(entity, 'device_class') %}{% if dc == 'motion' %}{{ 'Motion detected' if is_state(entity, 'on') else 'Clear' }}{% elif dc in ['door','garage_door','opening','window'] %}{{ 'Open' if is_state(entity, 'on') else 'Closed' }}{% else %}{{ 'Active' if is_state(entity, 'on') else 'Clear' }}{% endif %} · " + subtitle,
        "icon": icon,
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": MOD_SUBTLE,
        "visibility": vis(entity),
    }


def door_contact_card(entity, name="Front Door"):
    return {
        "type": "custom:mushroom-template-card",
        "entity": entity,
        "primary": name,
        "secondary": "{{ 'Open' if is_state(entity, 'on') else 'Closed' }} · Door contact",
        "icon": "mdi:door",
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": MOD_SUBTLE,
        "visibility": vis(entity),
    }


def weather_card():
    return {
        "type": "custom:mushroom-template-card",
        "entity": "weather.forecast_home",
        "primary": "{{ state_attr('weather.forecast_home','temperature') | round(0) }}°",
        "secondary": "{{ states('weather.forecast_home') | replace('_',' ') | title }}",
        "icon": "mdi:weather-partly-cloudy",
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": {**card_surface(), **MOD_TYPO_OFFICE},
        "visibility": vis("weather.forecast_home"),
    }


def alarm_card(compact=False):
    mod = MOD_TYPO_OFFICE if compact else MOD_TYPO_LABEL
    return {
        "type": "custom:mushroom-template-card",
        "entity": ALARM,
        "primary": "{{ states(entity) | replace('_',' ') | title }}",
        "secondary": "Security",
        "icon": "{% if is_state(entity, 'disarmed') %}mdi:shield-outline{% elif is_state(entity, 'triggered') %}mdi:shield-alert{% else %}mdi:shield-lock{% endif %}",
        "layout": "horizontal",
        "icon_color": "{% if is_state(entity, 'disarmed') %}grey{% else %}red{% endif %}",
        "tap_action": {"action": "more-info"},
        "card_mod": {
            "style": f"""
ha-card {{ background: {C['surface']}; border: 1px solid {C['stroke']}; box-shadow: none; border-radius: 16px; }}
{{% if not is_state('{ALARM}', 'disarmed') %}}
ha-card {{ background: rgba(255, 90, 90, 0.08) !important; border-color: rgba(255, 90, 90, 0.28) !important; }}
mushroom-shape-icon$ {{ --icon-color: {C['security']} !important; filter: drop-shadow(0 0 8px rgba(255,90,90,0.4)); }}
.primary {{ color: {C['security']} !important; font-weight: 500 !important; }}
{{% else %}}
.primary {{ color: {C['text_sec']}; }}
{{% endif %}}
""" + mod["style"]
        },
        "visibility": vis(ALARM),
    }


def doors_card(compact=False):
    mod = MOD_TYPO_OFFICE if compact else MOD_TYPO_LABEL
    return {
        "type": "custom:mushroom-template-card",
        "entity": "sensor.doors_status",
        "primary": "{{ states('sensor.doors_status') }}",
        "secondary": "Doors",
        "icon": "mdi:door-closed",
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": {
            "style": f"""
ha-card {{ background: {C['surface']}; border: 1px solid {C['stroke']}; box-shadow: none; border-radius: 16px; }}
{{% if states('sensor.doors_status') != 'All Closed' %}}
  mushroom-shape-icon$: {{ --icon-color: {C['security']} !important; }}
  .primary {{ color: {C['security']}; }}
{{% else %}}
  .primary {{ color: {C['text_sec']}; }}
{{% endif %}}
""" + mod["style"]
        },
        "visibility": vis("sensor.doors_status"),
    }


def media_card(entity, name="Media"):
    return {
        "type": "custom:mushroom-media-player-card",
        "entity": entity,
        "name": name,
        "use_media_info": True,
        "show_volume_level": False,
        "collapsible_controls": True,
        "layout": "horizontal",
        "icon": "mdi:cast",
        "card_mod": card_surface(),
        "visibility": vis(entity),
    }


def office_media_card(entity):
    """Spotify now-playing display with playback controls."""
    info = {
        "type": "custom:mushroom-template-card",
        "entity": entity,
        "primary": "{% set title = state_attr(entity, 'media_title') %}{% if title %}{{ title }}{% elif is_state(entity, 'playing') %}Playing{% elif is_state(entity, 'paused') %}Paused{% else %}Nothing playing{% endif %}",
        "secondary": "{% set artist = state_attr(entity, 'media_artist') %}{% set album = state_attr(entity, 'media_album_name') %}{% if artist and album %}{{ artist }} · {{ album }}{% elif artist %}{{ artist }}{% elif state_attr(entity, 'app_name') %}{{ state_attr(entity, 'app_name') }}{% else %}Spotify{% endif %}",
        "icon": "mdi:spotify",
        "layout": "horizontal",
        "icon_color": "green",
        "picture": "{{ state_attr(entity, 'entity_picture') }}",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 8px 4px 4px; }}
mushroom-shape-icon$ {{ --icon-size: 36px; --icon-color: {C['media']} !important; }}
mushroom-state-info$: |
  .primary {{ font-weight: 500; font-size: 17px; letter-spacing: 0.15px; color: {C['text']}; line-height: 1.25; }}
  .secondary {{ font-size: 12px; color: {C['text_sec']}; margin-top: 2px; }}
"""
        },
        "visibility": vis(entity),
    }
    controls = {
        "type": "custom:mushroom-media-player-card",
        "entity": entity,
        "name": "",
        "use_media_info": False,
        "show_volume_level": False,
        "collapsible_controls": True,
        "layout": "horizontal",
        "fill_container": True,
        "icon": "mdi:spotify",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 0 4px 8px; }}
mushroom-state-info$ {{ display: none; }}
"""
        },
        "visibility": vis(entity),
    }
    return {
        "type": "vertical-stack",
        "card_mod": card_surface("padding: 8px 12px; min-height: 156px;"),
        "cards": [info, controls],
    }


def weather_card_prominent():
    return {
        "type": "custom:mushroom-template-card",
        "entity": "weather.forecast_home",
        "primary": "{{ state_attr('weather.forecast_home','temperature') | round(0) }}°",
        "secondary": "{{ states('weather.forecast_home') | replace('_',' ') | title }}",
        "icon": "mdi:weather-partly-cloudy",
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": {
            "style": f"""
ha-card {{ background: {C['surface']}; border: 1px solid {C['stroke']}; box-shadow: none; border-radius: 16px; padding: 4px 0; }}
mushroom-shape-icon$ {{ --icon-color: {C['climate']} !important; opacity: 0.9; }}
mushroom-state-info$: |
  .primary {{ font-family: {FONT}; font-weight: 300; font-size: 28px; letter-spacing: 0.2px; color: {C['text']}; }}
  .secondary {{ font-family: {FONT}; font-weight: 400; font-size: 12px; color: {C['text_sec']}; }}
"""
        },
        "visibility": vis("weather.forecast_home"),
    }


def active_scene_card(select_entity="input_select.office_active_scene", label="Active Scene"):
    return {
        "type": "custom:mushroom-template-card",
        "entity": select_entity,
        "primary": "{% if is_state(entity, 'None') %}No scene active{% elif is_state(entity, 'Custom') %}Custom{% else %}{{ states(entity) }}{% endif %}",
        "secondary": label,
        "icon": "{% if is_state(entity, 'Custom') %}mdi:tune-vertical{% else %}mdi:palette-outline{% endif %}",
        "layout": "horizontal",
        "icon_color": "{% if is_state(entity, 'Custom') %}grey{% elif is_state(entity, 'None') %}grey{% else %}green{% endif %}",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 0; }}
{{% if is_state(entity, 'Custom') %}}
  .primary {{ color: {C['text_sec']}; font-weight: 400; font-size: 13px; }}
{{% elif not is_state(entity, 'None') %}}
  mushroom-shape-icon$ {{ --icon-color: {C['active']} !important; }}
  .primary {{ color: {C['text']}; font-weight: 500; }}
{{% else %}}
  .primary {{ color: {C['text_dis']}; font-weight: 400; font-size: 13px; }}
{{% endif %}}
"""
        },
    }


def all_lights_off_card():
    return quick_action_card(
        "All Lights Off",
        "Whole home",
        "mdi:lightbulb-off-outline",
        "light.turn_off",
        {"entity_id": "light.whole_house"},
    )


def quick_action_card(primary, secondary, icon, service, target=None, nav_path=None):
    card = {
        "type": "custom:mushroom-template-card",
        "primary": primary,
        "secondary": secondary,
        "icon": icon,
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": card_surface(),
    }
    if nav_path:
        card["tap_action"] = {"action": "navigate", "navigation_path": nav_path}
    else:
        card["tap_action"] = {"action": "call-service", "service": service}
        if target:
            card["tap_action"]["target"] = target
    return card


def nav_pill(name, path, icon, current_path, large=False):
    active = path == current_path
    height = 34 if large else 28
    font_size = 11 if large else 10
    icon_size = 15 if large else 13
    return {
        "type": "custom:mushroom-template-card",
        "primary": name,
        "secondary": "",
        "icon": icon,
        "layout": "horizontal",
        "tap_action": {"action": "navigate", "navigation_path": path},
        "card_mod": {
            "style": f"""
ha-card {{
  background: {'rgba(48,209,88,0.14)' if active else 'rgba(255,255,255,0.04)'} !important;
  border: none;
  box-shadow: none;
  border-radius: 14px;
  min-height: {height}px;
  height: {height}px;
  padding: 0 {'12px' if large else '10px'};
  margin: 0;
}}
mushroom-shape-icon$ {{ --icon-size: {icon_size}px; --icon-color: {C['active'] if active else C['text_dis']} !important; }}
.primary {{
  font-family: {FONT};
  font-size: {font_size}px;
  font-weight: {'500' if active else '400'};
  letter-spacing: 0.12px;
  white-space: nowrap;
  color: {C['text'] if active else C['text_sec']};
}}
.card-content {{ padding: 0 2px !important; }}
"""
        },
    }


def nav_pills(current_path):
    def nav_row(items, large=False):
        return {
            "type": "grid",
            "square": False,
            "columns": len(items),
            "cards": [nav_pill(n, p, ic, current_path, large=large) for n, p, ic in items],
            "card_mod": {
                "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; margin: 0; padding: 0; }}
#root {{ gap: {'8px' if large else '6px'} !important; }}
"""
            },
        }

    return {
        "type": "vertical-stack",
        "card_mod": {
            "style": "ha-card { background: transparent; border: none; box-shadow: none; margin: 0 0 14px; padding: 0; }"
        },
        "cards": [
            nav_row([NAV[0], NAV[3], NAV[4]]),
            nav_row([NAV[1], NAV[2]], large=True),
        ],
    }


def nav_bottom(current_path):
    return {
        "type": "vertical-stack",
        "card_mod": MOD_TRANSPARENT,
        "cards": [
            {
                "type": "custom:mushroom-template-card",
                "primary": "More",
                "secondary": "",
                "icon": "mdi:minus",
                "layout": "horizontal",
                "card_mod": {
                    "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 24px 2px 6px; margin: 0; }}
mushroom-shape-icon$ {{ display: none; }}
mushroom-state-info$: |
  .primary {{ font-family: {FONT}; font-weight: 500; font-size: 10px; letter-spacing: 0.8px; text-transform: uppercase; color: {C['text_dis']}; opacity: 0.7; }}
  .secondary {{ display: none; }}
"""
                },
            },
            {
                "type": "grid",
                "square": False,
                "columns": 3,
                "cards": [nav_pill(n, p, ic, current_path) for n, p, ic in NAV_SECONDARY],
                "card_mod": {
                    "style": "ha-card { background: transparent; border: none; box-shadow: none; margin: 0; padding: 0; } #root { gap: 6px !important; }"
                },
            },
        ],
    }


def nav_chips(current_path):
    return nav_pills(current_path)


def desktop_icon_nav(current_path):
    icons = []
    for name, path, icon in NAV:
        active = path == current_path
        icons.append({
            "type": "custom:mushroom-template-card",
            "primary": "",
            "secondary": "",
            "icon": icon,
            "layout": "vertical",
            "tap_action": {"action": "navigate", "navigation_path": path},
            "card_mod": {
                "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 6px 4px; min-height: 36px; }}
mushroom-shape-icon$ {{ --icon-color: {C['active'] if active else C['text_dis']} !important; --icon-size: 22px; }}
mushroom-state-info$ {{ display: none; }}
"""
            },
        })
    return {"type": "vertical-stack", "cards": icons, "card_mod": MOD_DESKTOP_ONLY}


def page_shell(current_path, content_cards, desktop_nav=True, shell_mod=None):
    """Desktop: optional slim icon rail + content. Mobile: full-width content only."""
    inner = {
        "type": "vertical-stack",
        "card_mod": MOD_PAGE_CONTENT,
        "cards": [nav_chips(current_path), *content_cards, nav_bottom(current_path)],
    }
    stack_cards = [inner]
    if desktop_nav:
        stack_cards.insert(0, desktop_icon_nav(current_path))
    return {
        "type": "horizontal-stack",
        "card_mod": shell_mod or MOD_SHELL,
        "cards": stack_cards,
    }


def status_grid():
    return {
        "type": "grid",
        "columns": 3,
        "square": False,
        "cards": [weather_card(), alarm_card(compact=True), doors_card(compact=True)],
        "card_mod": MOD_TRANSPARENT,
    }


def lights_section(pairs):
    return {
        "type": "vertical-stack",
        "card_mod": MOD_TRANSPARENT,
        "cards": [section_label("Lighting")] + [light_card(e, n) for e, n in pairs],
    }


def greeting_header():
    return {
        "type": "custom:mushroom-template-card",
        "primary": f"{{% if now().hour < 12 %}}Good morning, {OWNER_NAME}{{% elif now().hour < 18 %}}Good afternoon, {OWNER_NAME}{{% else %}}Good evening, {OWNER_NAME}{{% endif %}}",
        "secondary": "{{ now().strftime('%A · %H:%M') }}",
        "icon": "mdi:weather-night",
        "layout": "horizontal",
        "icon_color": "grey",
        "card_mod": {
            "style": f"""
ha-card {{ background: transparent; border: none; box-shadow: none; padding: 4px 0 8px; }}
mushroom-state-info$: |
  .primary {{ font-family: {FONT}; font-weight: 500; font-size: 20px; letter-spacing: -0.2px; color: {C['text']}; line-height: 1.3; }}
  .secondary {{ font-family: {FONT}; font-weight: 400; font-size: 12px; color: {C['text_sec']}; margin-top: 2px; }}
"""
        },
    }


def home_scene_grid():
    return all_lights_off_card()


def security_status_row():
    return {
        "type": "grid",
        "columns": 2,
        "square": False,
        "cards": [alarm_card(compact=True), doors_card(compact=True)],
        "card_mod": MOD_TRANSPARENT,
    }


def mobile_view(title, path_slug, current_path, cards):
    return {
        "title": title,
        "path": path_slug,
        "theme": THEME,
        "type": "panel",
        "cards": [page_shell(current_path, cards)],
    }


def office_panel():
    scene_chips = [scene_card_script(s, l, o, ic) for s, l, o, ic in OFFICE_SCENES]
    office_path = "/dashboard-office/office"
    content = [
        {
            "type": "horizontal-stack",
            "card_mod": MOD_TRANSPARENT,
            "cards": [
                weather_card(),
                alarm_card(compact=True),
                doors_card(compact=True),
                {
                    "type": "custom:mushroom-template-card",
                    "entity": "input_select.office_active_scene",
                    "primary": "{% if is_state(entity, 'None') %}No scene{% elif is_state(entity, 'Custom') %}Custom{% else %}{{ states(entity) }}{% endif %}",
                    "secondary": "Scene",
                    "icon": "{% if is_state(entity, 'Custom') %}mdi:tune-vertical{% else %}mdi:palette-outline{% endif %}",
                    "layout": "horizontal",
                    "icon_color": "{% if is_state(entity, 'Custom') %}grey{% elif is_state(entity, 'None') %}grey{% else %}green{% endif %}",
                    "card_mod": {
                        "style": f"""
ha-card {{ background: {C['surface']}; border: 1px solid {C['stroke']}; box-shadow: none; border-radius: 16px; }}
{{% if is_state(entity, 'Custom') %}}
  .primary {{ color: {C['text_sec']}; font-weight: 400; }}
{{% elif not is_state(entity, 'None') %}}
  mushroom-shape-icon$ {{ --icon-color: {C['active']} !important; }}
  .primary {{ color: {C['text']}; font-weight: 500; }}
{{% else %}}
  .primary {{ color: {C['text_sec']}; }}
{{% endif %}}
""" + MOD_TYPO_OFFICE["style"]
                    },
                    "visibility": vis("input_select.office_active_scene"),
                },
            ],
        },
        {"type": "horizontal-stack", "card_mod": MOD_TRANSPARENT, "cards": scene_chips[:3]},
        {"type": "horizontal-stack", "card_mod": MOD_TRANSPARENT, "cards": scene_chips[3:6]},
        responsive_stack(
            {
                "type": "vertical-stack",
                "card_mod": MOD_TRANSPARENT,
                "cards": [
                    section_label("Lighting"),
                    light_card(OFFICE_ALL_LIGHTS, "Office"),
                    light_card(OFFICE_HALO, "Halo", color_control=True),
                ],
            },
            {
                "type": "vertical-stack",
                "card_mod": MOD_TRANSPARENT,
                "cards": [
                    section_label("Sound"),
                    office_media_card("media_player.office_homepod_mini"),
                ],
            },
        ),
        {
            "type": "horizontal-stack",
            "card_mod": MOD_TRANSPARENT,
            "cards": [
                quick_action_card("All Off", "Office only", "mdi:power", "light.turn_off", {"entity_id": OFFICE_ALL_LIGHTS}),
                {
                    **sensor_card("sensor.office_office_battery", "Dimmer", "%", "mdi:battery-outline", "lighting"),
                    "card_mod": card_surface(),
                },
                door_contact_card("binary_sensor.front_door_sensor_open", "Front Door"),
                quick_action_card("Calendar", "F1 Season", "mdi:calendar-outline", None, nav_path="/calendar"),
            ],
        },
    ]
    return {
        "title": "Office",
        "path": "office",
        "theme": THEME,
        "type": "panel",
        "cards": [page_shell(office_path, content, desktop_nav=False, shell_mod=MOD_SHELL_OFFICE)],
    }


# ─── Dashboards ─────────────────────────────────────────────────────────────

overview = storage_dashboard("lovelace.lovelace", {
    "views": [{
        "title": "Home",
        "path": "default_view",
        "theme": THEME,
        "type": "panel",
        "cards": [page_shell("/lovelace/default_view", [
            greeting_header(),
            weather_card_prominent(),
            security_status_row(),
            section_label("Quick Actions"),
            all_lights_off_card(),
            section_label("Environment"),
            environment_card("sensor.home_average_temperature", "sensor.home_average_humidity", "Whole Home"),
            section_label("Lighting"),
            light_card("light.whole_house", "All Lights"),
            light_card("light.living_room_living_room", "Living Room"),
            section_label("Media"),
            media_card("media_player.office_homepod_mini", "HomePod"),
            section_label("Motion"),
            security_card("binary_sensor.hallway_motion_detected", "Hallway"),
            security_card("binary_sensor.kitchen_motion_detected", "Kitchen"),
            security_card("binary_sensor.living_room_motion_detected", "Living Room", subtitle="Eufy PIR"),
        ])],
    }],
})

bedroom = storage_dashboard("lovelace.dashboard_bedroom", {
    "views": [mobile_view("Bedroom", "bedroom", "/dashboard-bedroom/bedroom", [
        environment_card("sensor.temperature_temperature", "sensor.temperature_humidity", "Master Bedroom"),
        scene_grid([
            "scene.master_bedroom_master_bedroom_bedtime",
            "scene.master_bedroom_master_bedroom_nightlight",
            "scene.master_bedroom_master_bedroom_relax",
            "scene.master_bedroom_master_bedroom_read",
            "scene.master_bedroom_master_bedroom_reading",
            "scene.master_bedroom_master_bedroom_energise",
            "scene.master_bedroom_master_bedroom_concentrate",
            "scene.master_bedroom_master_bedroom_chilled_custom",
        ], columns=2),
        lights_section([("light.master_bedroom_master_bedroom", "All Lights")]),
        lights_section([("light.bathroom_bathroom", "Bathroom")]),
    ])],
})

living = storage_dashboard("lovelace.dashboard_living_room", {
    "views": [mobile_view("Living Room", "living-room", "/dashboard-living-room/living-room", [
        environment_card(
            "sensor.living_room_living_room_temperature_temperature",
            "sensor.living_room_living_room_temperature_humidity",
            "Living Room",
        ),
        scene_grid([
            "scene.living_room_living_room_relax",
            "scene.living_room_living_room_watching_tv",
            "scene.living_room_living_room_bright",
            "scene.living_room_living_room_nightlight",
            "scene.living_room_living_room_dimmed",
            "scene.living_room_living_room_read",
            "scene.living_room_living_room_working",
            "scene.living_room_living_room_bright_chill",
        ], columns=2),
        lights_section([
            ("light.living_room_living_room", "All Lights"),
            ("light.living_room_ceiling", "Ceiling"),
            ("light.living_room_pendants", "Pendants"),
            ("light.living_room_lamp", "Lamp"),
            ("light.living_room_hue_play_left", "Play Left"),
            ("light.living_room_hue_play_right", "Play Right"),
        ]),
        security_card("binary_sensor.living_room_motion_detected", "Motion"),
    ])],
})

office = storage_dashboard("lovelace.dashboard_office", {"views": [office_panel()]})

dressing = storage_dashboard("lovelace.dashboard_dressing_room", {
    "views": [mobile_view("Dressing", "dressing-room", "/dashboard-dressing-room/dressing-room", [
        environment_card(
            "sensor.dressing_room_temperature_temperature",
            "sensor.dressing_room_temperature_humidity",
            "Dressing Room",
        ),
        scene_grid([
            "scene.dressing_room_dressing_room_read",
            "scene.dressing_room_dressing_room_relax",
            "scene.dressing_room_dressing_room_nightlight",
        ], columns=2),
        lights_section([("light.dressing_room_dressing_room", "All Lights")]),
    ])],
})

dining = storage_dashboard("lovelace.dashboard_dining", {
    "views": [mobile_view("Dining", "dining-room", "/dashboard-dining/dining-room", [
        scene_grid([
            "scene.dining_dining_relax", "scene.dining_dining_read",
            "scene.dining_dining_nightlight", "scene.dining_dining_energise",
        ], columns=2),
        lights_section([
            ("light.dining_dining", "All Lights"),
            ("light.dining_room_ceiling", "Ceiling"),
            ("light.dining_room_lamps", "Lamps"),
        ]),
    ])],
})

kitchen = storage_dashboard("lovelace.dashboard_kitchen", {
    "views": [mobile_view("Kitchen", "kitchen", "/dashboard-kitchen/kitchen", [
        scene_grid([
            "scene.kitchen_kitchen_bright", "scene.kitchen_kitchen_nightlight",
            "scene.kitchen_kitchen_relax", "scene.kitchen_kitchen_dimmed",
        ], columns=2),
        lights_section([("light.kitchen_kitchen", "All Lights")]),
        sensor_card("sensor.thermostat_1_current_temperature", "Thermostat", "°", "mdi:thermometer", "heating"),
        security_card("binary_sensor.kitchen_motion_detected", "Motion"),
    ])],
})

hall = storage_dashboard("lovelace.dashboard_hall_landing", {
    "views": [mobile_view("Hall", "hall-and-landing", "/dashboard-hall-landing/hall-and-landing", [
        environment_card("sensor.hue_motion_sensor_1_downstairs_temperature"),
        environment_card("sensor.hue_motion_sensor_1_landing_temperature"),
        scene_grid([
            "scene.hallway_hallway_nightlight", "scene.landing_landing_nightlight",
            "scene.hallway_hallway_bright", "scene.entrance_zone_nightlight",
        ], columns=2),
        lights_section([
            ("light.hallway_hallway", "Hallway"),
            ("light.landing_landing", "Landing"),
            ("light.entrance_zone", "Entrance"),
            ("light.porch_porch", "Porch"),
        ]),
    ])],
})

security_home = storage_dashboard("lovelace.dashboard_home", {
    "views": [mobile_view("Security", "home", "/dashboard-home/home", [
        alarm_card(),
        doors_card(),
        {
            "type": "vertical-stack",
            "card_mod": MOD_TRANSPARENT,
            "cards": [
                section_label("Motion"),
                security_card("binary_sensor.hallway_motion_detected", "Hallway"),
                security_card("binary_sensor.kitchen_motion_detected", "Kitchen"),
                security_card("binary_sensor.living_room_motion_detected", "Living Room"),
                security_card("binary_sensor.landing_motion_detected", "Landing"),
                security_card("binary_sensor.front_door_motion_detected", "Front Door"),
            ],
        },
        light_card("light.whole_house", "All Lights"),
    ])],
})

temps = storage_dashboard("lovelace.dashboard_temperatures", {
    "views": [mobile_view("Climate", "temperatures", "/dashboard-temperatures/temperatures", [
        environment_card("sensor.home_average_temperature", "sensor.home_average_humidity", "Whole Home"),
        environment_card("sensor.temperature_temperature", "sensor.temperature_humidity", "Master Bedroom"),
        environment_card(
            "sensor.living_room_living_room_temperature_temperature",
            "sensor.living_room_living_room_temperature_humidity",
            "Living Room",
        ),
        environment_card(
            "sensor.dressing_room_temperature_temperature",
            "sensor.dressing_room_temperature_humidity",
            "Dressing Room",
        ),
    ])],
})

sidebar = {
    "version": 1, "minor_version": 1, "key": "lovelace_dashboards",
    "data": {"items": [
        {"id": "lovelace", "show_in_sidebar": True, "icon": "mdi:home-outline", "title": "Home", "require_admin": False, "mode": "storage", "url_path": "lovelace"},
        {"id": "dashboard_home", "show_in_sidebar": True, "icon": "mdi:shield-outline", "title": "Security", "require_admin": False, "mode": "storage", "url_path": "dashboard-home"},
        {"id": "dashboard_living_room", "show_in_sidebar": True, "icon": "mdi:sofa-outline", "title": "Living Room", "require_admin": False, "mode": "storage", "url_path": "dashboard-living-room"},
        {"id": "dashboard_bedroom", "show_in_sidebar": True, "icon": "mdi:bed-outline", "title": "Bedroom", "require_admin": False, "mode": "storage", "url_path": "dashboard-bedroom"},
        {"id": "dashboard_office", "show_in_sidebar": True, "icon": "mdi:monitor", "title": "Office", "require_admin": False, "mode": "storage", "url_path": "dashboard-office"},
        {"id": "dashboard_dining", "show_in_sidebar": True, "icon": "mdi:silverware-fork-knife", "title": "Dining", "require_admin": False, "mode": "storage", "url_path": "dashboard-dining"},
        {"id": "dashboard_kitchen", "show_in_sidebar": True, "icon": "mdi:stove", "title": "Kitchen", "require_admin": False, "mode": "storage", "url_path": "dashboard-kitchen"},
        {"id": "dashboard_dressing_room", "show_in_sidebar": False, "icon": "mdi:hanger", "title": "Dressing", "require_admin": False, "mode": "storage", "url_path": "dashboard-dressing-room"},
        {"id": "dashboard_hall_landing", "show_in_sidebar": False, "icon": "mdi:door-sliding", "title": "Hall", "require_admin": False, "mode": "storage", "url_path": "dashboard-hall-landing"},
        {"id": "dashboard_temperatures", "show_in_sidebar": False, "icon": "mdi:thermometer", "title": "Climate", "require_admin": False, "mode": "storage", "url_path": "dashboard-temperatures"},
        {"id": "map", "show_in_sidebar": False, "icon": "mdi:map-outline", "title": "Map", "require_admin": False, "mode": "storage", "url_path": "map"},
    ]},
}

lovelace_resources = {
    "version": 1, "minor_version": 1, "key": "lovelace_resources",
    "data": {"items": [
        {"id": "idium-card-mod", "url": f"/local/community/lovelace-card-mod/card-mod.js?{RESOURCE_TAG}", "type": "module"},
        {"id": "idium-mushroom", "type": "module", "url": f"/local/community/lovelace-mushroom/mushroom.js?{RESOURCE_TAG}"},
        {"id": "idium-minigraph", "type": "module", "url": f"/local/community/mini-graph-card/mini-graph-card-bundle.js?{RESOURCE_TAG}"},
    ]},
}

mapping = {
    ".storage/lovelace.lovelace": overview,
    ".storage/lovelace.dashboard_bedroom": bedroom,
    ".storage/lovelace.dashboard_living_room": living,
    ".storage/lovelace.dashboard_office": office,
    ".storage/lovelace.dashboard_dressing_room": dressing,
    ".storage/lovelace.dashboard_dining": dining,
    ".storage/lovelace.dashboard_kitchen": kitchen,
    ".storage/lovelace.dashboard_hall_landing": hall,
    ".storage/lovelace.dashboard_temperatures": temps,
    ".storage/lovelace.dashboard_home": security_home,
    ".storage/lovelace_dashboards": sidebar,
    ".storage/lovelace_resources": lovelace_resources,
}

if __name__ == "__main__":
    manifest = {path: json.dumps(data, indent=2) for path, data in mapping.items()}
    out_dir = REPO_ROOT / "dist"
    out_dir.mkdir(exist_ok=True)
    out = Path(os.environ.get("IDIUM_MANIFEST", out_dir / "ha_write_manifest.json"))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Idium Home Assistant {VERSION}: generated {len(manifest)} dashboard files → {out}")
