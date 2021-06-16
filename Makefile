patch:
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run --username ' ' --password ' '
	python3 -m pip install --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
install:
	poetry install