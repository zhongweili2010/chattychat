#apps/user_app/urls

from django.urls import re_path
from . import views
urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^login/$',views.login,name='login'),
    re_path(r'^logout/$',views.logout_user,name='logout'),
    re_path(r'^$',views.login_page,name='login_page'),
    re_path(r'^profile$',views.user_profile,name="profile"),
    re_path(r'^add_friend/(?P<number>\d+)$',views.add_friend,name="add_friend"),
]