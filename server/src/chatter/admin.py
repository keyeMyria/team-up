from django.contrib import admin

from chatter.models import Message, Room, ChatEvent

admin.site.register(Room)
admin.site.register(ChatEvent)
admin.site.register(Message)
