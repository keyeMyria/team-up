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
    public = models.BooleanField(default=False)
    name = models.TextField(_('Name of the room'), null=True, blank=True)
    users = models.ManyToManyField('accounts.User', blank=True)
    active_users = models.ManyToManyField('accounts.User', related_name='active_rooms', blank=True)
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

    def allowed(self, user):
        """
        Return True if user is allowed to join this room and False otherwise.
        """
        if user.room_set.filter(id=self.id).exists():
            return True
        else:
            return False


class ChatEvent(models.Model):
    EVENTS = (
        ('connect', _('connect')),
        ('disconnect', _('disconnect'))
    )

    event = models.TextField(choices=EVENTS)
    user = models.ForeignKey('accounts.User')
    room = models.ForeignKey(Room)
    date = models.DateTimeField(_('Date'), default=timezone.now)

    class Meta:
        verbose_name = 'Chat event'
        verbose_name_plural = 'Chat events'
        get_latest_by = 'date'
