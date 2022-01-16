import email
import datetime
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, UserForm, TwittForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from pymongo import MongoClient

db = MongoClient().bittertwitt_db

@login_required(login_url="login")
def user_list_view(request):
    username = request.user.username
    context ={"users":User.objects.all(), "username": username}
    return render(request,"users_view.html",context)

def index(request):
    username = request.user.username
    twitts = db.twitts.find()
    return render(request,"index.html", {"username": username, "twitts": twitts})

def user_registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        formUser = request.POST
        if form.is_valid():
            user = User(
                first_name= formUser['first_name'],
                last_name = formUser['last_name'],
                username = formUser['username'],
                email=formUser['email']
            )
            user.set_password(formUser['password'])
            user.save()
            return HttpResponseRedirect(reverse('users'))
    else:
        form = UserForm()
        return render(request,"user_registration.html",{'form':form})

@login_required(login_url="login")
def user_details(request,user_id):
    username = request.user.username
    user = db.auth_user.find_one({"id" : user_id})
    twitts = db.twitts.find({"autor": user['username']})

    initial_data = {
        'autor': request.user.username,
        'date': datetime.datetime.today()
    }
    
    form = TwittForm(request.POST or None, initial=initial_data)
    if request.method == "POST":
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.save()
            twittData = form.cleaned_data
            db.twitts.insert_one(twittData)
            print(form.cleaned_data)
    return render(request,"user_details.html",{"user":user, "twitts": twitts, "form": form, "username": username})

def login_view (request) :
    if request.method == 'POST':
        username = request.POST[ "username" ]
        password = request.POST[ "password" ]
        user = authenticate ( username=username , password=password )
        print(user)
        if user is not None :
            if user.is_active :
                print("dobre")
                login(request,user)
                return HttpResponseRedirect(reverse('users'))
            else:
                print("zbanowany")
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