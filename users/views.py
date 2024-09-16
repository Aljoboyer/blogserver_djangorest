from django.shortcuts import render
from . models import User
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.contrib.auth.hashers import check_password

# Create your views here.
@api_view(['GET'])
def AllUsers(request):
    ai = User.objects.all()

    serializer = UserSerializer(ai, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def Create_User(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        userData = serializer.save()

       #Generate JWT token for the newly created user
        refresh = RefreshToken.for_user(userData)
        access_token = str(refresh.access_token)

        return Response({
            'msg': 'User created successfully',
            'user': serializer.data,
            'refresh': str(refresh),
            'access': access_token,
        }, status=201)
    
    return Response(serializer.errors)

@api_view(['POST'])
def Login(request):
    requestData = request.data
    emaildata = requestData.get("email")
    password = requestData.get("password")
   
    try:
        # Find the user by email
        existsUser = User.objects.get(email=emaildata)
        
        # Check if the provided password matches the hashed password
        if check_password(password, existsUser.password):
            # Password is correct, serialize the user data
            serializer = UserSerializer(existsUser)

            #Generate JWT token for the newly created user
            refresh = RefreshToken.for_user(existsUser)
            access_token = str(refresh.access_token)
            
            return Response({
                'msg': 'Login successful',
                'data': serializer.data,
                'access_token': access_token
            }, status=status.HTTP_200_OK)
        else:
            # Password is incorrect
            return Response({
                'error': 'Invalid password'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    except ObjectDoesNotExist:
        createUserDict = {
            "email" : emaildata,
            "password" : password,
            "phone" : "03904543534",
            "about" : {
                "about" : "hello boss"
            },
        }
        serializer = UserSerializer(data=createUserDict)
        if serializer.is_valid():
            userData = serializer.save()

            #Generate JWT token for the newly created user
            refresh = RefreshToken.for_user(userData)
            access_token = str(refresh.access_token)
            return Response({
            'error': 'User not found with this email So I have Created New'
            })
        
