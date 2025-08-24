# Limiting Factors — Essay Template

A reproducible, citable data-essay scaffold for *Limiting Factors*.

## Quickstart

```bash
# 1) (Optional) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r env/requirements.txt

# 3) Reproduce figures and render the essay
make reproduce
```

Outputs: `figures/` and `_site/`.

## Repo layout
```
limiting-factors-essay-template/
├─ README.md
├─ METHODS.md
├─ CITATION.cff
├─ LICENSE
├─ .gitignore
├─ _quarto.yml
├─ essay.qmd
├─ Makefile
├─ env/
│  └─ requirements.txt
├─ data/
│  ├─ raw/
│  └─ processed/
├─ notebooks/
│  └─ analysis.qmd
├─ scripts/
│  ├─ 00_fetch.py
│  ├─ 01_clean.py
│  └─ 02_analyze.py
└─ figures/
```
