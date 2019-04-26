# chattychat/apps/chat_app/urls.py
from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add_friend/$', views.add_friend, name='add_friend'),
    re_path(r'^(?P<room_name>[^/]+)/$',views.room,name='room'),
]