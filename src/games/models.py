from django.db import models
from django.utils.text import ugettext_lazy as _


class GameAccount(models.Model):
    username = models.TextField(max_length=100)

    class Meta:
        abstract = True


class LeagueOfLegendsAccount(GameAccount):
    LEAGUE_CHOICES = (
        ('Bronze', _('Bronze')),
        ('Silver', _('Silver')),
        ('Gold', _('Gold')),
        ('Platinum', _('Platinum')),
        ('Diamond', _('Diamond')),
        ('Master', _('Master')),
        ('Challenger', _('Challenger'))
    )
    DIVISION_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
    )

    league = models.TextField(_('User\'s league'), choices=LEAGUE_CHOICES)
    division = models.TextField(_('User\'s division'), choices=DIVISION_CHOICES)

    class Meta:
        verbose_name = 'League of Legends account'
        verbose_name_plural = 'League of Legends accounts'
