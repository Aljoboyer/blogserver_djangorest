from django.shortcuts import render
from . models import User
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

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