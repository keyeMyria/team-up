from django.contrib import admin

from chat.models import Message, Room, ChatEvent, TemporaryToken

admin.site.register(Room)
admin.site.register(ChatEvent)
admin.site.register(Message)
admin.site.register(TemporaryToken)
