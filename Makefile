.PHONY: test start stop

test:
	pipenv run ./manage.py test

docker-start:
	docker-compose up

docker-stop:
	docker-compose stop

docker-build:
	docker-compose build

docker-test:
	docker-compose run app wait-for-postgres.sh db pipenv run ./manage.py test

docker-cov:
	docker-compose run app wait-for-postgres.sh db "pipenv run coverage run manage.py test && pipenv run coverage report && pipenv coverage html"
