build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down --remove-orphans
remove-db:
	docker-compose down --remove-orphans -v
migrate:
	docker exec app_web_1 python manage.py migrate
makemigrations:
	docker exec app_web_1 python manage.py makemigrations
collectstatic:
	docker exec app_web_1 python manage.py collectstatic --no-input --clear