#chattychat/urls.py
from django.contrib import admin
from django.urls import path,include,re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^chat/',include('apps.chat_app.urls')),
    re_path(r'^login/',include('apps.user_app.urls')),
]
