from chat.consumers import ChatConsumer


channel_routing = [
    ChatConsumer.as_route(path=r'^/chat/(?P<room_id>\d+)/$')
]
