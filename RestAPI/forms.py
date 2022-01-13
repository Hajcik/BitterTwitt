from django import forms
from django.contrib.auth.models import User

from RestAPI.models import Twitt

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['title', 'content', 'autor']