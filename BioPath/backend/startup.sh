#!/bin/bash

while !</dev/tcp/db/5432 # busy wait until port 5432 is open so that we can succesfully connect to db
    do
        sleep 1
    done

python manage.py makemigrations # TODO this probably shouldn't be done every time
python manage.py migrate # TODO same as this
python manage.py load_data
python manage.py runserver 0.0.0.0:8000