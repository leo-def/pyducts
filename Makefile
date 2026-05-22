# Variables
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python
UVICORN = $(VENV)/bin/uvicorn
PYTEST = $(VENV)/bin/pytest
RUFF = $(VENV)/bin/ruff

.PHONY: all
all: build

# Setup virtual environment and install dependencies
.PHONY: install
install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Alias for installation
.PHONY: build
build: install

# Run FastAPI dev server
.PHONY: dev
dev:
	$(UVICORN) src.main:app --reload

# Run pytest suite
.PHONY: test
test:
	PYTHONPATH=src $(PYTEST)

# Lint code using Ruff
.PHONY: lint
lint:
	$(RUFF) check .

# Clean temporary Python cache directories
.PHONY: clean
clean:
	rm -rf $(VENV)/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache/ .ruff_cache/
