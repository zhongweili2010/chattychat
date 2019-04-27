# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth.decorators import login_required
from .models import Message
from ..user_app.models import User
from channels.auth import login,logout
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        self.room_group_name = 'chat_%s' % self.room_name
        
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # async_to_sync(login)(self.scope,self.scope['user'])
        # self.scope["session"].save()
        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': str(self.scope['user'].first_name)+' entered the room',
            }
        )


    def disconnect(self, close_code):   
        # Leave room group
        print('leaving the room!!!!!')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': str(self.scope['user'].first_name)+' left the room',
            }
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        # async_to_sync(logout)(self.scope)
    
    
    
    
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


        
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        Message.objects.create(content=message,sender=self.user)
        message=str(self.scope['user'].first_name)+ ' says: '+message
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
