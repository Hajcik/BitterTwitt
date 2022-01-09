from django.shortcuts import render

from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .forms import UserForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login

from pymongo import MongoClient

db = MongoClient().bittertwitt_db

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

def user_details(request,user_id):
    user = db.auth_user.find_one({"id" : user_id})
    return render(request,"user_details.html",{"user":user})