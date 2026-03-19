# Stratum — Full-Stack Development from First Principles

Course source files. Built with [Sphinx](https://www.sphinx-doc.org/) and
deployed to GitHub Pages.

## Local setup

**Requirements:** Python 3.10+, PlantUML on PATH.

Install PlantUML:

```bash
# macOS
brew install plantuml

# Ubuntu / Debian
sudo apt-get install plantuml

# Windows
choco install plantuml
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Build the site:

```bash
make html
# Output: _build/html/index.html
```

Live preview with auto-reload (requires `sphinx-autobuild`):

```bash
pip install sphinx-autobuild
make livehtml
```

## Deployment

Pushing to `main` triggers the GitHub Actions workflow at
`.github/workflows/deploy.yml`, which builds the site and pushes
the output to the `gh-pages` branch.

**GitHub Pages configuration (one-time):**

1. Go to repository Settings → Pages
2. Set source to **Deploy from a branch**
3. Set branch to `gh-pages`, folder to `/ (root)`
4. Save

## Project structure

```
stratum-course/
├── docs/                  ← Sphinx source root
│   ├── conf.py            ← Sphinx configuration
│   ├── index.md           ← Course entry point
│   ├── before_you_begin.md
│   ├── level-1/
│   ├── level-2/
│   ├── level-3/
│   ├── level-4/
│   └── level-5/
├── _build/                ← Build output (gitignored)
├── .github/workflows/
│   └── deploy.yml         ← GitHub Actions deployment
├── requirements.txt
├── Makefile
└── README.md
```

## Authoring

- All lesson files are Markdown (`.md`), processed by MyST parser
- Diagrams: Mermaid for flow/sequence/ER; PlantUML for C4/component/deployment/use case
- Callout boxes: `> [!NOTE]`, `> [!WARNING]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!CAUTION]`
- See `BLUEPRINT.md` for full authoring rules and lesson template
