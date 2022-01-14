from django.contrib import admin
from django.apps import AppConfig
from RestAPI.models import Twitt
# Register your models here.
admin.site.register(Twitt)

class RestAPIConfig(AppConfig):
    name = 'rest_api'