from django.contrib import admin
from django.apps import AppConfig
from RestAPI.models import User, Twitt
# Register your models here.
admin.site.register(User)
admin.site.register(Twitt)

class RestAPIConfig(AppConfig):
    name = 'rest_api'