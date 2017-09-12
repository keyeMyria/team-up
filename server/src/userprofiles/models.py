from django.db import models

from games.models import GameAccount


class UserProfile(models.Model):
    user = models.OneToOneField('accounts.User')

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return f'userprofile: {self.user.username}'

    @property
    def accounts(self):
        """
        :return: User's active games accounts
        """
        account_names = [cls.__name__ for cls in GameAccount.__subclasses__()]
        accounts = {acc_name: getattr(self, f'{acc_name.lower()}_set').all()
                    for acc_name in account_names}
        return accounts
