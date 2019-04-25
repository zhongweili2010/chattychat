#chattychat/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import apps.chat_app.routing

application=ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            apps.chat_app.routing.websocket_urlpatterns
        )
    )
})