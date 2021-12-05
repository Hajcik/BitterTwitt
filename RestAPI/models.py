from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255,blank=False, default='')
    last_name = models.CharField(max_length=255,blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Twitt(models.Model):
    content=models.CharField(max_length=280,blank=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)