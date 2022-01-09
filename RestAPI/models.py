from django.db import models

# Create your models here.

class User(models.Model):
    _id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,blank=False, default='')
    last_name = models.CharField(max_length=255,blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    nick = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=255, blank=False, default='')

class Twitt(models.Model):
    _id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=64,blank=False)
    content=models.TextField(max_length=255,blank=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)