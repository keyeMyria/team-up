from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from chat.bindings import MessageBinding


class APIDemultiplexer(WebsocketDemultiplexer):
    consumers = {
        'messages':  MessageBinding.consumer
    }


channel_routing = [
    route_class(APIDemultiplexer)
]
