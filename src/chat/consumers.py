from channels.generic.websockets import JsonWebsocketConsumer

from common.authentication import RestTokenConsumerMixin
from common.mixins import KeepUserConsumerMixin


class ChatConsumer(RestTokenConsumerMixin,
                   KeepUserConsumerMixin,
                   JsonWebsocketConsumer):

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def connect(self, message, **kwargs):
        """
        Perform things on connection start
        """
        if message.user is not None and message.user.is_authenticated():
            message.reply_channel.send({"accept": True})
        else:
            self.close({'Error': 'Not authenticated user'})

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Simple echo
        self.send(self.user.username)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass
