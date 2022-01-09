from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Twitt(models.Model):
    _id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=64,blank=False)
    content=models.TextField(max_length=255,blank=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)