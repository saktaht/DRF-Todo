docker compose up --build --detach

docker exec -it drf /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

ユーザー名: admin

メールアドレス: fjla32@gmail.com

パスワード: fafa86487

トークン発行

curl -X POST http://0.0.0.0:8000/api-auth/login/ \
-H "Content-Type: application/json" -d ' { "username": "admin", "password": "fafa86487" }'

curl -X POST http://0.0.0.0:8000/api-auth/logout/ -H "Authorization: Bearer 発行されたトークン"

docker compose down --rmi all -v
