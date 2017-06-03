from django.db import models
from django.utils.text import ugettext_lazy as _


class GameAccount(models.Model):
    username = models.TextField(max_length=100)

    class Meta:
        abstract = True


class LeagueOfLegendsAccount(GameAccount):
    LEAGUE_CHOICES = (
        (1, _('Bronze')),
        (2, _('Silver')),
        (3, _('Gold')),
        (4, _('Platinum')),
        (5, _('Diamond')),
        (6, _('Master')),
        (7, _('Challenger'))
    )
    DIVISION_CHOICES = (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
    )

    league = models.PositiveIntegerField(_('User\'s league'), choices=LEAGUE_CHOICES)
    division = models.PositiveIntegerField(_('User\'s division'), choices=DIVISION_CHOICES)

    class Meta:
        verbose_name = 'League of Legends account'
        verbose_name_plural = 'League of Legends accounts'
