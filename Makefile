build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down --remove-orphans
remove-db:
	docker-compose down --remove-orphans -v
migrate:
	docker exec e-commerce_web_1 python manage.py migrate
makemigrations:
	docker exec e-commerce_web_1 python manage.py makemigrations
read-transactions:
	docker-compose exec web python manage.py runscript run_read_transactions
init:
	docker-compose up -d
	docker exec e-commerce_web_1 python manage.py migrate
shell:
	docker-compose exec web python manage.py shell
