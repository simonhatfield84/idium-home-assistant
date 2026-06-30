# Contributing to Idium Home Assistant

Thank you for your interest in Idium Home Assistant. This project aims to be a polished, community-maintained dashboard system — not a personal Home Assistant dump.

## Design freeze (v1.0.x)

**Visual design is frozen for v1.0.x.** Please do not open PRs that change colours, spacing, card layouts, or navigation patterns without prior discussion.

Allowed without prior approval:

- Bug fixes (broken templates, wrong entity references in examples)
- Documentation improvements
- Generator portability (config, clearer customization points)
- CI, packaging, HACS metadata
- Optional helpers (behind examples / flags)

Requires an issue with **design-review** label first:

- New dashboard sections or layout changes
- Theme token changes
- Navigation structure changes

## Development setup

```bash
git clone https://github.com/simonhatfield84/idium-home-assistant.git
cd idium-home-assistant
cp config/idium.example.json config/idium.json
./scripts/generate.sh
python3 -m py_compile generator/idium_gen.py
```

No runtime dependencies beyond Python 3.9+ standard library.

## Pull request process

1. Fork the repository and create a feature branch from `main`
2. Update documentation if you change behaviour
3. Add a CHANGELOG entry under `[Unreleased]` (or the appropriate version)
4. Ensure `./scripts/generate.sh` succeeds
5. Open a PR with a clear description of the change

## Commit messages

Use clear, imperative subjects:

- `Fix alarm card template when entity is unavailable`
- `Document HACS theme installation`
- `Add office_room_lights to example config`

## Code style

- Python: PEP 8, 4-space indent, type hints welcome in new code
- YAML: 2-space indent
- Markdown: wrap prose for readability; keep line length reasonable

## Licensing

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Questions

Open a [Discussion](https://github.com/simonhatfield84/idium-home-assistant/discussions) or issue if you are unsure whether a change fits the design freeze.
