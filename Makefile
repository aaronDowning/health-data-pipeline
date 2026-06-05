PYTHON = .venv/bin/python
PYTEST = .venv/bin/pytest

.DEFAULT_GOAL := help

.PHONY: help install test run clean ci

help:
	@echo ""
	@echo "  make install   create venv and install dependencies"
	@echo "  make test      run all tests with verbose output"
	@echo "  make run       run the pipeline on sample data"
	@echo "  make clean     remove generated output files"
	@echo "  make ci        run what CI runs (tests only)"
	@echo ""

install:
	python3.12 -m venv .venv
	$(PYTHON) -m pip install --upgrade pip --quiet
	$(PYTHON) -m pip install -r requirements.txt --quiet
	@echo "Done. Activate with: source .venv/bin/activate"

test:
	PYTHONPATH=src $(PYTEST) -v

run:
	PYTHONPATH=src $(PYTHON) run.py

clean:
	rm -rf output/
	@echo "Output cleared."

ci:
	PYTHONPATH=src $(PYTEST)
