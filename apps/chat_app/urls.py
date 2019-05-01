# chattychat/apps/chat_app/urls.py
from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add_friend/$', views.add_friend, name='add_friend'),
    re_path(r'^unfriend/(?P<number>\d+)/$',views.unfriend,name='unfriend'),
    re_path(r'^multi_friend/$',views.multi_friend,name="multi_friend"),
    re_path(r'^add_group/$',views.enter_room),
    re_path(r'^leave_group/(?P<room_id>\d+)/$',views.leave_group),
    re_path(r'^(?P<room_name>[^/]+)/$',views.room),
    
]