from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import UserSerializer

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
def get_user(request, user_token):
	token = Token.objects.filter(key=user_token).first()
	user = token.user
	serializer = UserSerializer(user)
	return Response(serializer.data)

	
@api_view(['GET', 'POST'])
def change_password(request, user_token):

	current_password = request.data.get('current_password')
	new_password = request.data.get('new_password')

	token = Token.objects.filter(key=user_token).first()
	user = token.user
	check_user = authenticate(request, username=user.username, password=current_password)

	if check_user:
		user.set_password(new_password)
		user.save()
		return Response(True)
	else:
		return Response(False)
