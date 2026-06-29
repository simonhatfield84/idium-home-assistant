# Publishing to GitHub

Minimal steps to publish Idium as a public repository.

## Before you push

1. Replace `YOUR_ORG` in:
   - `README.md`
   - `CHANGELOG.md`
   - `CONTRIBUTING.md`
   - `SECURITY.md` (add real contact emails)
   - `CODE_OF_CONDUCT.md`
2. Capture real screenshots → `docs/screenshots/*.png` → update README image links
3. Review `packages/idium_helpers.yaml.example` entity IDs

## Create repository

```bash
cd ~/Projects/idium
git add -A
git status
git commit -m "Release Idium v1.0.0"
git tag -a v1.0.0 -m "Idium v1.0.0 — initial public release"
git remote add origin git@github.com:YOUR_ORG/idium.git
git push -u origin main
git push origin v1.0.0
```

## GitHub release

1. **Releases → Draft new release** → tag `v1.0.0`
2. Title: **Idium v1.0.0**
3. Paste `CHANGELOG.md` section for 1.0.0
4. Attach screenshots (optional)
5. Publish

## HACS

Users add custom repository:

- URL: `https://github.com/YOUR_ORG/idium`
- Category: **Theme**

For full dashboards, point users to `docs/installation.md`.

## CI

GitHub Actions workflow `.github/workflows/validate.yml` runs on push/PR.

## Design freeze

Tag v1.0.0 marks the frozen design baseline. See `CONTRIBUTING.md`.
