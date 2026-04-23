run:
	.venv/bin/uvicorn src.main:app --reload

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

test:
	PYTHONPATH=. .venv/bin/pytest

lint:
	.venv/bin/ruff check .
