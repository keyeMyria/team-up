from django.contrib.auth import get_user_model


class KeepUserConsumerMixin:
    channel_session = True

    @staticmethod
    def _save_user(func):
        def wrapper(message, **kwargs):
            if message.user is not None and message.user.is_authenticated():
                message.channel_session['user_id'] = message.user.id
            return func(message, **kwargs)
        return wrapper

    def __getattribute__(self, name):
        method = super().__getattribute__(name)
        if name == 'connect':
            return self._save_user(method)
        return method

    @property
    def user(self):
        user_id = self.message.channel_session['user_id']
        return get_user_model().objects.get(id=user_id)
