from channels_api.bindings import ResourceBinding

from oauth2_provider.models import AccessToken
from accounts.models import User

from .models import Message
from .serializers import MessageSerializer


class MessageBinding(ResourceBinding):
    model = Message
    stream = 'messages'
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    @classmethod
    def trigger_inbound(cls, message, **kwargs):
        """
        Triggers the binding to see if it will do something.
        Also acts as a consumer.
        """
        if message.channel.name == 'websocket.connect':
            message.user = User.objects.all()[0]
        return super().trigger_inbound(message, **kwargs)


