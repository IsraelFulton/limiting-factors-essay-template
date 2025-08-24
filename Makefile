.PHONY: env data analyze figures render reproduce clean

env:
	python -m venv .venv && . .venv/bin/activate && pip install -r env/requirements.txt

data:
	. .venv/bin/activate && python scripts/00_fetch.py && python scripts/01_clean.py

analyze:
	. .venv/bin/activate && python scripts/02_analyze.py

figures: analyze
	@echo "Figures written by analysis to ./figures"

render:
	. .venv/bin/activate && quarto render essay.qmd

reproduce: env data figures render

clean:
	rm -rf figures/* data/processed/* _site/
