release: mkdir -p gestao_escolar/staticfiles && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT
