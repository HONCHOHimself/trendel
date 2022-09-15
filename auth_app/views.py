from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET', 'POST'])
def login_view(request):

    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = authenticate(request, username=username, password=password)
        token = Token.objects.filter(user=user).first()
        return Response(token.key)
    except:
        return Response(False)


@api_view(['GET', 'POST'])
def register_view(request):

    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(email=email).exists():
        return Response('Email Address already exists.')
    else:
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            token = Token(user=user)
            token.save()
            return Response(True)
        except:
            return Response('User already exists.')
