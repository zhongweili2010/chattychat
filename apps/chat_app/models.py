from django.db import models
from ..user_app.models import User

class Message(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='messages')
    





# class messages(models.Model):
#     message = models.TextField()
#     sender = models.ForeignKey(User,on_delete=SET_NULL)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     reciever = models.ForeignKey(User,on_delete=SET_NULL)

# Create your models here.
