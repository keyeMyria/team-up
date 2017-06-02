from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.text import ugettext_lazy as _


class Message(models.Model):
    room = models.ForeignKey('chat.Room')
    sender = models.ForeignKey('accounts.User')
    content = models.TextField(_('Content of the message'))
    date = models.DateTimeField(_('Date'), default=timezone.now)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        get_latest_by = 'date'

    def __str__(self):
        return f'{self.sender} : {self.date} : {self.content}'


class Room(models.Model):
    name = models.TextField(_('Name of the room'))
    users = models.ManyToManyField('accounts.User')
    date_created = models.DateTimeField(_('Date'), default=timezone.now)

    class Meta:
        verbose_name = 'room'
        verbose_name_plural = 'rooms'
        get_latest_by = 'date_created'

    def __str__(self):
        return self.name

    @property
    def last_activity(self):
        try:
            return self.message_set.latest()
        except ObjectDoesNotExist:
            return None
