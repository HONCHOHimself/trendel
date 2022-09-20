from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ProfilePicture

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
