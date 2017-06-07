from django.contrib.auth import get_user_model


class KeepUserConsumerMixin:
    """
    Make it possible to keep information about the user after initial connection
    when not provided by channels (eg. when using tokens as authentication).
    Must be placed before WebsocketConsumer (or derivative) in inheritance.
    """
    channel_session = True

    def dispatch(self, message, **kwargs):
        response = super().dispatch(message, **kwargs)
        if message.channel.name == 'websocket.connect':
            if message.user is not None and not message.user.is_anonymous:
                message.channel_session['user_id'] = message.user.id
        return response

    @property
    def user(self):
        user_id = self.message.channel_session['user_id']
        return get_user_model().objects.get(id=user_id)
