build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down --remove-orphans
remove-db:
	docker-compose down --remove-orphans -v
migrate:
	docker exec e_commerce_app_web_1 python manage.py migrate
makemigrations:
	docker exec e_commerce_app_web_1 python manage.py makemigrations
read-transactions:
	docker-compose exec web python manage.py runscript run_read_transactions
populate-counter:
	docker-compose exec web python manage.py runscript run_populate_counter
populate_high_attention_article:
	docker-compose exec web python manage.py runscript run_populate_high_attention_article
init:
	docker-compose up -d
	docker exec e_commerce_app_web_1 python manage.py migrate
	docker-compose exec web python manage.py runscript run_read_transactions
	docker-compose exec web python manage.py runscript run_populate_counter
	docker-compose exec web python manage.py runscript run_populate_high_attention_article
shell:
	docker-compose exec web python manage.py shell
