# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json
from django.contrib.auth.decorators import login_required
from .models import Message,Client,ChatGroup
from ..user_app.models import User

from channels.auth import login,logout
from channels.layers import get_channel_layer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if Client.objects.filter(user=self.user).count()>0:
            Client.objects.get(user=self.user).delete()
        this_channel=Client.objects.create(channel_name=self.channel_name,user=self.user)
        
        self.group_list=[]

        #add current channel to all groups it suppose be on
        if ChatGroup.objects.filter(users=self.user).count() >0:
            for group in ChatGroup.objects.filter(users=self.user).all():
                group_name=str(group.id)
                self.group_list.append(group_name)
                print(f"added to group{group.id}")
                await self.channel_layer.group_add(
                    group_name,
                    self.channel_name
                )
                print(self.group_list)

            
        
        

        # self.user_name = self.scope['url_route']['kwargs']['user_name']
        # # self.room_name=self.scope['url_route']['kwargs']['room_name']
        print(f"user {self.channel_name} connected")
        # if self.user_name!=self.user.username:
        #     print('not same user')
        
        # self.room_group_name = 'chat_%s' % self.room_name  

        # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.accept()

    async def disconnect(self, close_code):   
        Client.objects.get(user=self.user).delete()
        # # Leave room group
        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message = f"{self.user.username} said : "+message
        #send one to one to channel layer
        if text_data_json['type']=='direct_message':
            user_id=text_data_json['receiver']

            friend=User.objects.get(id=int(user_id))
            try :
                friend_channel=friend.client_of.channel_name
                await self.channel_layer.send(friend_channel, {
                    "type": 'chat.message',
                    "message":message,
                    "sender_id":self.user.id,
                })
            except:
                await self.channel_layer.send(self.channel_name,{
                    "type":'chat.message',
                    "message": "user cannot be reached at this moment",
                    "sender_id":receiver,
                })


        #sending group message to channel_layer
        elif text_data_json['type']=='group_message':
            # group=ChatGroup.objects.get(id=int(text_data_json[reciever]))
            await self.channel_layer.group_send(
                text_data_json['receiver'],
                {
                    "type":"chat_message",
                    "message":message,
                    "group":text_data_json['receiver'],
                    
                })


    #Receive from channel layer
    async def chat_message(self, event):
        if "sender_id" in event:
            message = event['message']
            sender_id=event['sender_id']

            await self.send(text_data=json.dumps({
                'type': 'chat.message',
                'message': message,
                'sender_id': sender_id,
            }))
        #message from group to websocket
        elif "group" in event:
            message=event['message']
            group_id=event['group']      
            await self.send(text_data=json.dumps({
                'type':'group.message',
                'message': message,
                'group_id':group_id,
            }))  
            print(message)

            # 'room_id': room_id,
            # 'channel_name':self.channel_name,
      
