# Generated by Django 2.0.2 on 2018-02-27 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.TextField(choices=[('connect', 'connect'), ('disconnect', 'disconnect')])),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Chat event',
                'verbose_name_plural': 'Chat events',
                'get_latest_by': 'datetime',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content of the message')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False)),
                ('name', models.TextField(blank=True, null=True, verbose_name='Name of the room')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('active_users', models.ManyToManyField(blank=True, related_name='active_rooms', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'room',
                'verbose_name_plural': 'rooms',
                'get_latest_by': 'date_created',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatevent',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Room'),
        ),
        migrations.AddField(
            model_name='chatevent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
