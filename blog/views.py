from django.shortcuts import render
from . models import Blog
from . serializers import BlogSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PublishBlog(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        blogdata = serializer.save()

        return Response({
            'msg': 'Blog created successfully',
            'blog': serializer.data,
        }, status=201)
    
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddComment(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        # blogdata = serializer.save()
        serializer.save(commenter=request.user)

        return Response({
            'msg': 'Blog created successfully',
            'blog': serializer.data,
        }, status=201)
    
    return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SingleBlog(request, pk=None):
   
    # singleUserData = User.objects.get(id=pk)
    blog = get_object_or_404(Blog.objects.prefetch_related('comments'), id=pk)  # Prefetch blogs for the user
    serializer = BlogSerializer(blog)

    return Response(serializer.data)