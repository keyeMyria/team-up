# from channels.generic.websockets import WebsocketDemultiplexer
# from channels.routing import route_class
#
# from chat.bindings import MessageBinding
#
#
# class APIDemultiplexer(WebsocketDemultiplexer):
#     consumers = {
#         'messages':  MessageBinding.consumer
#     }
#
#
# channel_routing = [
#     route_class(APIDemultiplexer)
# ]


from chat.consumers import MyConsumer


channel_routing = [
    MyConsumer.as_route(path=r"^/chat/")
]
