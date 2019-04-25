# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import admin
from .models import User as User

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User,UserAdmin)

# Register your models here.
