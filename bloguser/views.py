from django.shortcuts import render
from . models import User
from . serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from blogsetting.models import BlogSettings
from blogsetting.serializers import BlogSettingSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllUsers(request):
   
    ai = User.objects.all()

    serializer = UserSerializer(ai, many = True, fields=['id', 'name', 'email', 'phone', 'profileImg'])

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def Create_User(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        userData = serializer.save()
        print('userdata', userData)

        if userData:
            settingsJson = {"blogcount": 0, "paymentVerified": False}
            serializer2 = BlogSettingSerializer(data=settingsJson)

            if serializer2.is_valid():
                serializer2.save(user=userData)

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
@permission_classes([AllowAny])
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
            serializer = UserSerializer(existsUser, fields=['id', 'name', 'email', 'phone', 'profileImg'])

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
        return Response({
                'error': 'User With this email does not exists'
            }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SingleUser(request, pk=None):
   
    # singleUserData = User.objects.get(id=pk)
    user = get_object_or_404(User.objects.prefetch_related('blogs'), id=pk)  # Prefetch blogs for the user
    serializer = UserSerializer(user)

    return Response(serializer.data)
