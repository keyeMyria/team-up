from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('accounts.User')
    account_league_of_legends = models.ForeignKey('games.LeagueOfLegendsAccount', blank=True,
                                                  null=True)

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
        accounts = []
        for attr in dir(self):
            if attr.startswith('account'):
                account = getattr(self, attr)
                if account is not None:
                    accounts.append(account)
        return accounts
