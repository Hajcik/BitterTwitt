from rest_framework import serializers 
from RestAPI.models import Twitt, User
  
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name')
               
class TwittSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Twitt
        fields = ('id',
                  'content')