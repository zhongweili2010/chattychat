from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager as AbstractUserManager
from django.contrib.auth import authenticate,login

import re
import datetime as dt

import random
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(AbstractUserManager):
    # def create_superuser(self,password)

    def validate(self,postData):
        error={}
        if len( postData['first_name'] )<3:
            error['first_name']='first_name should be more than 2 chars'
            print('first_name bad')
        if len( postData['last_name'] )<3:
            error['last_name']='last_name should be more than 2 chars'
            print('last_name bad')
        if not EMAIL_REGEX.match(postData['email']):
            error['email']='email format not valid'
            print('emailbad')
        elif User.objects.filter(email=postData['email']).count()>0:
            error['email']='email taken, sorry!'
            print('emailbad')
        if len(postData['birthday'])<1:
            error['birthday']='birthday cannot be empty'
            print('birthdaybad')
        else:
            birthday=dt.datetime.strptime(postData['birthday'],"%Y-%m-%d")
            if birthday>dt.datetime.today():
                error['birthday']='you have not been born yet'
                print('birthdaybad')
            elif dt.datetime.today()- birthday < dt.timedelta(days=365*13):
                error['birthday']='too young too simple'
                print('birthdaybad')

        if len( postData['password'] )<8:
            error['password']='password cannot be shorter than 8'
        if postData['password']!=postData['password_re']:
            error['password_re']='password not matching'
        return error

    # def login(self,postData):
    #     error={}
    #     if not EMAIL_REGEX.match(postData['email']):
    #         error['email_login']='email format not valid'
    #         return error
    #     elif User.objects.filter(email=postData['email']).count()==0:
    #         error['email_login']='login failed'
    #         return error
    #     else:
    #         user=authenticate(request,username=request.POST['email'],password=request.POST['password'])
    #         if user is not None:
    #             login(request,user)


    #         if bcrypt.checkpw(postData['password'].encode(),this_user.password.encode()):
    #             return this_user
    #         else:
    #             error['email_login']='login failed'
    #             return error

class User(AbstractUser):
    
    # interest=models.CharField(max_length=25) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # password=models.CharField(max_length=80)
    birthday=models.DateTimeField(null=True)
    # single=models.BooleanField(null=True)
    # bio=models.TextField(null=True)
    objects=UserManager()
# Create your models here.

