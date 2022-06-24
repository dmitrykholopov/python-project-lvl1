# Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python3 -m pip install --user /Users/dmitrykholopov/HEXLET/python-project-lvl1/dist/hexlet_code-0.1.7-py3-none-any.whl

package-uninstall:
	python3 -m pip uninstall /Users/dmitrykholopov/HEXLET/python-project-lvl1/dist/hexlet_code-0.1.7-py3-none-any.whl

lint:
	poetry run flake8 /Users/dmitrykholopov/HEXLET/python-project-lvl1/brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc
