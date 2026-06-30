# Security

This repo is themes, a dashboard generator, and example YAML. Nothing runs on its own — you copy it into your Home Assistant config.

If you spot something unsafe in the generator, scripts, or example packages, email **simonhatfield@me.com** rather than opening a public issue. I'll reply when I can.

**Out of scope:** Home Assistant Core bugs ([report there](https://github.com/home-assistant/core/security)), third-party HACS cards.

**Obvious but worth saying:** don't commit real tokens or internal URLs in `config/idium.json`. Read any `packages/*.yaml` before pasting into a live system.
