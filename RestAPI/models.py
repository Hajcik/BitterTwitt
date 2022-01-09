from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255,blank=False, default='')
    last_name = models.CharField(max_length=255,blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    nick = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=255, blank=False, default='')

    def __str__(self):
        return "{} {}".format(self.email)

class Twitt(models.Model):
    title=models.CharField(max_length=64,blank=False)
    content=models.TextField(max_length=255,blank=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)