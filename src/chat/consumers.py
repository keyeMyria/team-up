from channels.generic.websockets import JsonWebsocketConsumer
from common.authentication import RestTokenConsumerMixin


class MyConsumer(RestTokenConsumerMixin, JsonWebsocketConsumer):

    # Set to True if you want it, else leave it out
    strict_ordering = False
    http_user = True

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
        self.message.reply_channel.send({"accept": True})

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Simple echo
        self.send(self.message.user.username)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass