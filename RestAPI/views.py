from django.shortcuts import render

from django.http.response import HttpResponseRedirect
from django.urls import reverse

from RestAPI.models import Twitt

from .forms import LoginForm, UserForm, TwittForm

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required

from pymongo import MongoClient

db = MongoClient().bittertwitt_db

@login_required(login_url="login")
def user_list_view(request):
    context ={"users":User.objects.all()}
    
    return render(request,"users_view.html",context)

def index(request):
    return render(request,"index.html")

def user_registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users'))
    else:
        form = UserForm()
        return render(request,"user_registration.html",{'form':form})

@login_required(login_url="login")
def user_details(request,user_id):
    user = db.auth_user.find_one({"id" : user_id})
    twitts = db.twitts.find({"autor": user['username']})
    form = TwittForm()
    return render(request,"user_details.html",{"user":user, "twitts": twitts, "form":form})

def login_view (request) :
    if request.method == 'POST':
        username = request.POST[ "username" ]
        password = request.POST[ "password" ]
        user = authenticate ( username=username , password=password )
        if user is not None :
            if user.is_active :
                login(request,user)
                return HttpResponseRedirect(reverse('users'))
            else:
                form = LoginForm()
                print("zbanowany uzytkownik")
                return render(request,"login.html",{'form':form})
        else:
            print("zle passy")
            form = LoginForm()
            return render(request,"login.html",{'form':form})
    else:
        form = LoginForm()
        return render(request,"login.html",{'form':form})

@login_required(login_url="login")
def logout_view (request) :
    logout(request)
    return HttpResponseRedirect('login')


def postTwitt (request, userId):
    if request.method == "POST":
        form = TwittForm(request.POST)
        if form.is_valid():
            autor = get_object_or_404(User,pk=userId)
            twitt = Twitt(title=form.cleaned_data.get("title"),content=form.cleaned_data.get("content"),autor=autor)
            twitt.save()
    return render(request,"user_details.html",{'user_id':userId})