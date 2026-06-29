# Security Policy

## Supported versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a vulnerability

**Please do not open public GitHub issues for security vulnerabilities.**

Email the maintainers (replace with your contact before publishing):

- **security@your-domain.example**

Include:

- Description of the issue
- Steps to reproduce
- Impact assessment
- Suggested fix (if any)

We aim to acknowledge reports within **72 hours** and provide a fix timeline within **14 days** for confirmed issues.

## Scope

In scope:

- Idium generator scripts (`generator/`, `scripts/`)
- Example packages that could lead to unsafe HA configuration if copied blindly
- Documentation that instructs insecure deployment (e.g. exposing secrets)

Out of scope:

- Home Assistant Core vulnerabilities (report to [Home Assistant](https://github.com/home-assistant/core/security))
- Third-party HACS cards (Mushroom, card-mod, mini-graph-card)

## Safe deployment reminders

- Never commit `config/idium.json` with real tokens or internal URLs
- Restrict file-system / SSH access to your HA host
- Review `packages/*.yaml` before merging into your live config
