from django.shortcuts import render
from . models import User
from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def Create_User(request):
    serializer = UserSerializer(data=request.data)
    print('Request ==>',serializer)

    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Successfully Insert Done'}

        return Response(res)
    
    return Response(serializer.errors)