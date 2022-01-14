from rest_framework import serializers 
from RestAPI.models import Twitt
                 
class TwittSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Twitt
        fields = ('id',
                  'content')