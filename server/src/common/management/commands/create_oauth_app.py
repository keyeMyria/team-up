from django.core.management.base import BaseCommand

from oauth2_provider.models import Application
from accounts.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Application.objects.filter(name='Team-up').exists():
            uid = User.objects.get(username='admin').id
            Application.objects.create(
                name='Team-up',
                authorization_grant_type='password',
                client_type='confidential',
                user_id=uid)
