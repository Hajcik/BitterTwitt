from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200,blank=False, default='')
    last_name = models.CharField(max_length=200,blank=False, default='')