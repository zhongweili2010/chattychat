#chattychat/urls.py
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from apps.user_app.models import User
from apps.chat_app.models import Message
from apps.user_app.views import UserViewSet

router=routers.DefaultRouter()
router.register(r'user',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^chat/',include('apps.chat_app.urls')),
    re_path(r'^login/',include('apps.user_app.urls')),
    re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    re_path(r'^logout/',include('apps.user_app.urls')),

]
urlpatterns+=router.urls
