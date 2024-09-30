from django.shortcuts import render
from . models import BlogSettings
from . serializers import BlogSettingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PaymentVerfying(request):
    serializer = BlogSettingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response({
            'msg': 'Payment verified successfully',
            'payment': serializer.data,
        }, status=201)
    
    return Response(serializer.errors)
