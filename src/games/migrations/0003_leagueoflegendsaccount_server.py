# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20170606_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='leagueoflegendsaccount',
            name='server',
            field=models.PositiveIntegerField(choices=[(1, 'North America'), (2, 'EU West'), (3, 'EU Nordic & East'), (4, 'Latin America North'), (5, 'Latin America South'), (6, 'Brazil'), (7, 'Turkey'), (8, 'Russia'), (9, 'Oceania'), (10, 'Japan'), (11, 'Korea')], default=1, verbose_name="User's server"),
            preserve_default=False,
        ),
    ]