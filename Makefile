linter:
	poetry run pre-commit install && poetry run pre-commit run -a -v

tester:
	poetry run pytest tests