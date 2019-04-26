#chat_app/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from django.core.signals import request_finished
from ..user_app.models import User
@login_required(login_url='/login')
def index(request):
    return render(request,'chat_app/index.html',{'this_user':request.user})


@login_required(login_url='/login')
def room(request,room_name):
    # user_logged_in.send(User,user=request.user)

    return render(request,'chat_app/room.html',{
        'room_name_json':mark_safe(json.dumps(room_name))
    })

# @receiver(user_logged_in)
# def friend_loged_in(sender,user,**kwargs):
#     this_user=request
#     current_user=request.user
#     # print(this_user.first)
#     print(f"your friend {this_user.first_name}is logged on")





# Create your views here.

