from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from base.form import  BlogForm1,UserForm,userdetailForm
from base.models import blogpost, userdetail
# Create your views here.

def home(request):
    Post=blogpost.objects.all()
    context={"Post":Post}
    return render(request,'base/home.html',context)

def loginpage(request):

    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is None:
             messages.error(request,"Username and Password is invalid")
        else:
            login(request,user)
            return redirect("home")



    return render(request,'base/login.html')

def register(request):

    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]

        if password==password1 :
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exists")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email already exists")       
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    login(request,user)
                    userd=userdetail(about="",aboutuser=user,profile="")
                    userd.save()
                    return redirect("home")
        else:
            messages.error(request,"password not matching..")
            return redirect("register")
    

    return render(request,'base/register.html')

def logoutpage(request):

    auth.logout(request)
    return redirect("/")

def profile(request,pk):
    user=User.objects.get(pk=pk)
    userabout=userdetail.objects.get(aboutuser=pk)
    posts=blogpost.objects.filter(author=user)
    return render(request,"base/profile.html",{"userabout":userabout,"posts":posts,"user":user})

def editprofile(request):
    form = UserForm(instance=request.user)
    user_about,created= userdetail.objects.get_or_create(aboutuser=request.user)
    if user_about.about is None:
        create=userdetailForm()
    else:
        create=userdetailForm(instance=user_about)


    if request.method == "POST":
        if 'about' or 'profile' in request.POST:  # Check if the "about" section is being edited
            aboutform = userdetailForm(request.POST, request.FILES, instance=user_about)
            if aboutform.is_valid():
                aboutform.save()
            else:
                messages.error(request, "About form is not valid.")
       
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():   
            mail = form.cleaned_data['email']
            if User.objects.filter(email=mail).exclude(pk=request.user.pk).exists():
                messages.error(request, "Email address already exists.")
            else:
                form.save()
                return redirect('profile',request.user.pk) 
        else:
            messages.error(request, "User form is not valid.")

    return render(request, 'base/editprofile.html', {"form": form, "aboutform":create})

def createblog(request):

    if request.method=="POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        form=blogpost(img=image,content=content,title=title,author=request.user)
        form.save()
        return redirect("/")
    
        


    return render(request,'base/createblog.html')

def postview(request,pk):
    if request.user.is_authenticated:
        
        view="postview"
        posts=blogpost.objects.filter(pk=pk)
        aboutuser=userdetail.objects.filter(aboutuser=pk)
        
        context={"posts":posts,"about":aboutuser,"view":view} 
    else:
        return redirect('login')
    return render(request,'base/postview.html',context)

def authorpost(request,pk):
    view="authorpost"
    posts=blogpost.objects.filter(author=pk)
    aboutuser=userdetail.objects.filter(aboutuser=pk)
    
    context={"posts":posts,"about":aboutuser,"view":view}
    return render(request,'base/postview.html',context)

def postedit(request,pk):
    posts=blogpost.objects.filter(pk=pk)
    form=BlogForm1(instance=posts)

    return render()

def deletepost(request,pk):
    post=blogpost.objects.filter(pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("/")

    return render(request,'base/delete.html',{"post":post})

def editpost(request,pk):
    post=blogpost.objects.filter(pk=pk).first()
    form=BlogForm1(instance=post)

    if request.method=="POST":
        form=BlogForm1(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.error(request,"Form is invalid make sure image file length would be short ")
            return redirect("editpost",pk)
    return render(request,'base/editpost.html',{"form":form})

