from rest_framework import routers,serializers,viewsets
from apps.user_app.models import User
from apps.chat_app.models import Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Message
        fields=(
            'url',
            'content',
            'sender'
            )
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.Objects.all()
    serializer_class=MessageSerializer

router=routers.DefaultRouter()
router.register(r'messages',MessageViewSet)

        