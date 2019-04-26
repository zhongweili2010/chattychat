from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
#import models
from apps.user_app.models import *


@login_required(login_url='/login')
def index(request):
    context = {
        "this_user" : request.user,
        "all_users" : User.objects.all().exclude(id = request.user.id),
        "all_friends" : request.user.friends.all(),
    }
    return render(request,'chat_app/index.html',context)


@login_required(login_url='/login')
def room(request,room_name):
    this_email = request.user.email
    print(this_email)
    context = {
        "room_name_json" : mark_safe(json.dumps(room_name)),
        "this_user_json" : mark_safe(json.dumps(this_email)),
    }

    return render(request,'chat_app/room.html', context)

def add_friend(request):
    if request.method=="POST":
        #logic to add user
        this_user = request.user
        print("this user is:", this_user)
        friend_id = request.POST["add_friend"]
        this_friend = User.objects.get(id=friend_id)
        print("this friend is:", this_friend)
        this_user.friends.add(this_friend)
        return redirect('/chat')

# Create your views here.

