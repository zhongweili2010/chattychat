from django.shortcuts import render, redirect,HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
#import models
from apps.user_app.models import *
from ..user_app.models import User


@login_required(login_url='/login')
def index(request):
    context = {
        "this_user" : request.user,
        "all_users" : User.objects.all().exclude(id = request.user.id),
        "all_friends" : request.user.friends.all(),
        "this_user_json" : mark_safe(json.dumps(request.user.email)),
    }
    return render(request,'chat_app/index.html',context)


@login_required(login_url='/login')
def room(request,room_name):
    this_email = request.user.first_name
    context = {
        
        "room_name_json" : mark_safe(json.dumps(room_name)),
        "this_user_json" : mark_safe(json.dumps(this_email)),
    }

    return render(request,'chat_app/room.html', context)
@login_required(login_url='/login')
def add_friend(request):
    if request.method=="POST":
        #logic to add user
        this_user = request.user
        print("this user is:", this_user)
        friend_id = request.POST["add_friend"]
        this_friend = User.objects.get(id=friend_id)
        print("this friend is:", this_friend)
        if this_friend!=this_user:
            this_user.friends.add(this_friend)
            return redirect('/chat')
        else:
            return HttpResponse('cannot allow self add')
    else:
        return HttpResponse('bad post')



@login_required(login_url='/login')
def multi_friend(request):
    context={
        'all_friends':request.user.friends.all(),
        'this_user':request.user,

    }
    return render(request,'chat_app/platform.html',context)


# @receiver(user_logged_in)
# def friend_loged_in(sender,user,**kwargs):
#     this_user=request
#     current_user=request.user
#     # print(this_user.first)
#     print(f"your friend {this_user.first_name}is logged on")





# Create your views here.

