#chat_app views
from django.shortcuts import render, redirect,HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
#import models
from apps.user_app.models import *
from ..user_app.models import User
from .models import ChatGroup,Client
from channels.layers import get_channel_layer
from django.db.models import Q


@login_required(login_url='/login')
def index(request):

    #select users that not friend with self nor self
    all_friends=request.user.friends.all()
    all_friends_ids=[x.id for x in all_friends]
    all_nonfriends=User.objects.exclude(Q(id__in=all_friends_ids) | Q(id=request.user.id))
    print(all_nonfriends)

    
    context = {
        "this_user" : request.user,
        "all_nonfriends" : all_nonfriends,
        "all_friends" : request.user.friends.all(),
        "this_user_json" : mark_safe(json.dumps(request.user.email)),
        "all_groups":ChatGroup.objects.filter(users=request.user)
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
def unfriend(request,number):
    this_friend=User.objects.get(id=number)
    request.user.friends.remove(this_friend)
    return redirect('/chat')


# @login_required(login_url='/login')
# def multi_friend(request):
#     context={
#         'all_friends':request.user.friends.all(),
#         'this_user':request.user,

#     }
#     return render(request,'chat_app/platform.html',context)


@login_required(login_url='/login')
def enter_room(request):
    if request.method=="POST":
        room_name=request.POST['room_name']
        if ChatGroup.objects.filter(name=room_name).count()>0:
            this_group=ChatGroup.objects.filter(name=room_name).first()
        else:
            this_group=ChatGroup.objects.create(name=room_name)
        this_group.users.add(request.user)
        return redirect('/chat')
    else:
        return HttpResponse('bad post')
    
@login_required(login_url='/login')
def leave_group(request,room_id):
    this_group=ChatGroup.objects.get(id=room_id)
    this_group.users.remove(request.user)
    return redirect('/chat')


