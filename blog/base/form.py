from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from base.models import blogpost,userdetail

class BlogForm1(ModelForm):
    class Meta:
        model=blogpost
        fields=["title","content","img"]

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        
class userdetailForm(ModelForm):
    class Meta:
        model=userdetail
        fields=['about','profile']  