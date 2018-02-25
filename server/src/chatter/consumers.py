from channels.generic.websocket import JsonWebsocketConsumer


class ChatConsumer(JsonWebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection. Either call
        self.accept()

    def receive_json(self, content, **kwargs):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send_json({'data': content})
        # Or, to send a binary frame:
        self.send(bytes_data="Hello world!")

    def disconnect(self, close_code):
        pass
