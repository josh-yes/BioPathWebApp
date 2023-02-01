docker_run:
	docker-compose down
	docker-compose build
	docker-compose up

# docker_test:
# 	pg_ctl stop
# 	docker-compose down
# 	docker-compose build
# 	docker-compose up

local_run:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

local_test:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py test