from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json




@login_required(login_url='/login')
def index(request):
    return render(request,'chat_app/index.html',{})


@login_required(login_url='/login')
def room(request,room_name):
    return render(request,'chat_app/room.html',{
        'room_name_json':mark_safe(json.dumps(room_name))
    })

# Create your views here.

