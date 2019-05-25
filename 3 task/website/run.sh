#!/bin/sh

python /app/manage.py makemigration
python /app/manage.py migrate
exec python /app/manage.py runserver