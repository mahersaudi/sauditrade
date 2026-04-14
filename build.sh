#!/usr/bin/env bash
# Render Build Script for Saudi Export & Trade Council
set -o errexit

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🗂️  Collecting static files..."
python manage.py collectstatic --no-input

echo "🗃️  Running database migrations..."
python manage.py migrate

echo "🌱 Loading sample data (if database is empty)..."
python manage.py shell -c "
from exports.models import Category
if Category.objects.count() == 0:
    exec(open('exports/sample_data.py').read())
    print('Sample data loaded.')
else:
    print('Data already exists, skipping.')
"

echo "👤 Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@saudiexports.sa')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser \"{username}\" created.')
else:
    print(f'Superuser \"{username}\" already exists.')
"

echo "✅ Build complete!"

