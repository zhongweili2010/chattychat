# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import admin
from .models import User as User
from ..chat_app.models import Message
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message,MessageAdmin)
# Register your models here.
