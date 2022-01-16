import datetime
from tkinter import DISABLED
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Twitt(models.Model):
    _id = models.AutoField(primary_key=True)
    content=models.TextField(max_length=280,blank=False, default="Wpisz komentarz tutaj...")
    autor = models.CharField(max_length=200,blank=False)
   # autor = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(("Date"))