from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from base.models import blogpost,userdetail

class BlogForm1(ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control' "rows:4"}))

    
    class Meta:
        model=blogpost
        fields=["title","content","img"]
class BlogForm(ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model=blogpost
        fields="__all__"
    

class UserForm(ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'profile-input'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'profile-input'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'profile-input'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'profile-input'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        
class userdetailForm(ModelForm):
    #about=forms.CharField(widget=forms.TextInput(attrs={'class':'profile-input'}))
    #prfile=forms.ImageField(widget=forms.FileInput(attrs={'class':'profile-input'}))
    class Meta:
        model=userdetail
        fields=['about','profile']  

