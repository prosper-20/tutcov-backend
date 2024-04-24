import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
    # accept connection
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['department']
        self.room_group_name = f'chat_{self.id}'
        # join room group
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
        )

    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # send message to room group
        await self.channel_layer.group_send(
        self.room_group_name,
        {
        'type': 'chat_message',
        'message': message,
        'user': self.user.username,
        'datetime': now.isoformat(),
        }
        )

    # send message to WebSocket
        # self.send(text_data=json.dumps({'message': message}))


    # receive message from room group
    async def chat_message(self, event):
    # send message to WebSocket
        await self.send(text_data=json.dumps(event))