.PHONY: setup audit
.SILENT: setup audit

setup:
	python3 -m venv --clear .venv
	source .venv/bin/activate && \
	python -m pip install -U pip setuptools wheel && \
	python -m pip install flake8

audit:
	source .venv/bin/activate && \
	python -m flake8 .
