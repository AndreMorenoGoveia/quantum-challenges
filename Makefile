PY=python

setup:
	$(PY) -m pip install -U pip
	$(PY) -m pip install -e . || $(PY) -m pip install -r requirements.txt
	pre-commit install || true

test:
	pytest challenges/$(CHALLENGE)/tests -q

run:
	@echo "Running $(CHALLENGE) on $(BACKEND)"
	$(PY) challenges/$(CHALLENGE)/solution-$(BACKEND)/run.py

lint:
	ruff check . || true
