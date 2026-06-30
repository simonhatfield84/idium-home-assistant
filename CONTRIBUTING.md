# Contributing

Thanks for looking at this. It's mostly my home setup that I've put online in case it's useful — not a product with a roadmap team behind it.

## What I'm happy to merge

- Bug fixes (broken templates, wrong examples)
- Documentation that's clearer or more accurate
- Generator tweaks that make it easier to adapt to other homes
- CI / packaging fixes

## What needs a chat first

I'm not really looking to redesign the UI in v1.0. If you want to change colours, layout, or navigation, open an issue and we can talk before you spend time on a PR.

## Local setup

```bash
git clone https://github.com/simonhatfield84/idium-home-assistant.git
cd idium-home-assistant
cp config/idium.example.json config/idium.json
./scripts/generate.sh
python3 -m py_compile generator/idium_gen.py
```

Python 3.9+, stdlib only.

## Pull requests

1. Branch from `main`
2. Update docs if behaviour changes
3. Add a line to `CHANGELOG.md` under `[Unreleased]` if it's user-visible
4. Check `./scripts/generate.sh` still runs

By contributing you agree your changes are MIT-licensed like the rest of the repo.

Questions: open an issue or discussion.
