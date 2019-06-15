.PHONY: test start stop

test:
	pipenv run ./manage.py test

start:
	docker-compose up

stop:
	docker-compose stop

build:
	docker-compose build
