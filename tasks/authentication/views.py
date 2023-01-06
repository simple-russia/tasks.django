from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from . import serializers



@api_view(['GET'])
def ping(request):
    print(request.COOKIES)
    return Response('pong')


@swagger_auto_schema(request_body=serializers.LoginSerializer, methods=['POST'], responses={200: serializers.UserSerializer})
@api_view(['POST'])
def login_user(request):
    print('req->', request, type(request), 'orig:', request._request, type(request._request))
    # return user info too
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    data = serializer.validated_data
    username = data['username']
    password = data['password']
    
    # login
    user = authenticate(username=username, password=password)

    if user is not None:
        print(user)
        login(request, user)
    else:
        return Response('user not found', status=404)

    user_data = serializers.UserSerializer(user).data

    return Response(user_data)


@api_view(['POST'])
def logout():
    # return user info too
    return Response('logout')


@swagger_auto_schema(request_body=serializers.RegisterSerializer, methods=['POST'], responses={200: serializers.UserSerializer})
@api_view(['POST'])
def register(request):
    # register, login and return the user's info on success
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    username = data['username']
    password = data['password']

    if User.objects.filter(username=username).exists():
        return Response('This username is taken', status=400)

    user = User.objects.create_user(username=username, password=password)

    user_data = serializers.UserSerializer(user).data
    login(request, user)

    return Response(user_data, status=201)


@api_view(['POST'])
def change_password():
    return Response('change password')
