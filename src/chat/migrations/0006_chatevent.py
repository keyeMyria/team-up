# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_auto_20170610_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.TextField(choices=[('connect', 'connect'), ('disconnect', 'disconnect')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chat event',
                'verbose_name_plural': 'Chat events',
                'get_latest_by': 'date',
            },
        ),
    ]
