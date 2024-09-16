docker compose up --build --detach

docker exec -it django /bin/bash

python manage.py makemigrations accounts

python manage.py migrate

python manage.py createsuperuser

docker compose down --rmi all -v