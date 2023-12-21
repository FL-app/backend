#!/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Create superuser"
python manage.py shell -c "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@mail.com', 'password')"

# echo "Create users"
# python manage.py shell -c "from users.models import CustomUser; CustomUser.objects.create_user(email='user1@mail.com', username='user1', password='testpass1')"

echo "Starting Gunicorn."
exec gunicorn backend.wsgi:application --bind 0:8000 --workers 3
