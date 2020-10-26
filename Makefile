install:
	poetry install

lint:
	poetry run flake8 auto_clicker

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish:
	poetry publish -r test_pypi

.PHONY: install lint selfcheck check build publish