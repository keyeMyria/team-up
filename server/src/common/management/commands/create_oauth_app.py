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
                user_id=uid,

                # hardcoded for development
                client_id='za5Co8eueO0OgV9hXhIbbOWGVShpOJYB3Jgnia5z',
                client_secret=(
                    '0FK0oQQJu1TAlcJ1ZhOPgk3en0KLJdB8'
                    'pgaqnAMovz52FJxjdwpFmU1Qt1dUtFEQ'
                    'QFEYI4frmj7gCvfRBAff2ll9h7hf1aEB'
                    'BC4Wvtwjb2HBuBOefNZBLJAZhsfDDOEm'
                )
            )
