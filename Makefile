runserver-local: migrate
	python manage.py runserver --settings=settings.dev

newmigrations:
	python manage.py makemigrations --settings=settings.dev

migrate:
	python manage.py migrate --settings=settings.dev

environment:
	.\env\Scripts\Activate.ps1

createsuperuser:
	python manage.py createsuperuser --settings=settings.dev

tests:
	python manage.py test --settings=settings.dev

test-one:
	python manage.py test $(TEST_NAME) --settings=settings.dev

shellplus:
	python manage.py shell-plus --ipython --settings=settings.dev