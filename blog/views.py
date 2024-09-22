from django.shortcuts import render
from . models import Blog
from . serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def PublishBlog(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        blogdata = serializer.save()

        return Response({
            'msg': 'Blog created successfully',
            'blog': serializer.data,
        }, status=201)
    
    return Response(serializer.errors)
