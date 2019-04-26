#user_app/serializers.py

from rest_framework import routers,serializers,viewsets
from apps.user_app.models import User
from apps.chat_app.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    messages=MessageSerializer(many=True)
    class Meta:
        model=User
        fields=(
            'id',
            'messages',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'is_staff',

        )