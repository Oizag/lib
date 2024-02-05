# Including commands
run-django-server:
	poetry run task server localhost:8000

install-backend:
	poetry run pip install -U setuptools
	poetry install --no-root

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

.PHONY: makemigrations
makemigrations:
	poetry run task makemigrations

# Primary commands
.PHONY: install
install:
	@make install-backend
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin

.PHONY: install-prod
install-prod:
	poetry run pip install -U pip
	@make install-backend
	poetry run task initconfig

.PHONY: run
run:
	@make run-django-server

.PHONY: build
build:
	poetry run task collectstatic
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures
