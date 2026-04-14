import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create superuser from environment variables if not exists'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email    = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@saudiexports.sa')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

        if User.objects.filter(username=username).exists():
            self.stdout.write(f"  Superuser '{username}' already exists.")
        else:
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f"  ✅ Superuser '{username}' created."))

