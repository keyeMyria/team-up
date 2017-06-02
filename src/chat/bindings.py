from channels_api.bindings import ResourceBinding

from .models import Message
from .serializers import MessageSerializer


class MessageBinding(ResourceBinding):
    model = Message
    stream = 'messages'
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
