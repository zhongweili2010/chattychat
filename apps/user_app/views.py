from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import User
from django.urls import reverse
from django.contrib.auth import login as lg,logout,authenticate
from django.contrib.auth.decorators import login_required
import re


def login_page(request):
    # User.objects.calling()
    return render(request,'user_app/login_page.html')


def register(request):
    if request.method=="POST":
        errors=User.objects.validate(request.POST)
        if errors:
            for key,value in errors.items():
                messages.info(request,value,extra_tags=key)
            return redirect( reverse('login_page'))
        else:
            User.objects.create_user(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                username=request.POST['email'],
                password=request.POST['password'],
            )
            print('user created')
            
            return redirect( reverse('login_page'))
    else:
        return HttpResponse('bad post')
def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.info(request,'log in failed',extra_tags='email_login')
    else:
        user=authenticate(request,username=username,password=password)
        if user is not None:
            lg(request,user)
            return redirect('/chat')
        else:
            messages.info(request,'log in failed',extra_tags='email_login')        
    return redirect('/login/logout')


def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect('/login')

@login_required(login_url='/login')
def test(request):
    return HttpResponse('test site here')

@login_required(login_url='/login')
def success(request):
    return render(request,'login_and_registration/success.html')


