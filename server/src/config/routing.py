from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chatter.consumers import ChatConsumer
from common.authentication import OAuthTokenAuthMiddleware

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": OAuthTokenAuthMiddleware(
        URLRouter([
            path('chat/', ChatConsumer)
        ])
    )

})
