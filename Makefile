lint: flake8 mypy

flake8:
	flake8 --config setup.cfg ./

mypy:
	cd src && mypy --config-file ../setup.cfg ./