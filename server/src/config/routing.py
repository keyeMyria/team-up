from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # ChatConsumer.as_route(path=r'^/chat/(?P<room_id>\d+)/$')
        ])
    )

})
