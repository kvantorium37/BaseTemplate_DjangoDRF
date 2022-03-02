all: lint test
lint: flake8 mypy
test: pytest

flake8:
	flake8 --config setup.cfg ./

mypy:
	cd src && mypy --config-file ../setup.cfg ./

pytest:
	cd src && pytest