from django.shortcuts import render
from . models import Blog
from . serializers import BlogSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from blogsetting.models import BlogSettings
from blogsetting.serializers import BlogSettingSerializer
from bloguser.models import User
from bloguser.serializers import UserSerializer

# Create your views here.
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def PublishBlog(request):
#     userid = request.data["user"]
#     blogsetting = BlogSettings.objects.get(user=userid)

#     blogSettignSerial = BlogSettingSerializer(blogsetting)

#     serializer = BlogSerializer(data=request.data)
    
#     if blogSettignSerial.data["paymentVerified"] == True:
#         if serializer.is_valid():
            
#             blogdata = serializer.save(user=request.user)
            
#             if blogdata:
#                 blogCountIncrease = blogSettignSerial.data["blogcount"] + 1

#                 settingsJson = {"blogcount": blogCountIncrease}

#                 settingSerializer = BlogSettingSerializer(blogSettignSerial.data, data=settingsJson, partial=True)

#                 if settingSerializer.is_valid():
#                     settingSerializer.save()
#                     return Response({
#                         'msg': 'Blog created successfully',
#                         'blog': serializer.data,
#                     }, status=201)
                
#         return Response(serializer.errors)
#     return Response({"msg" : "Payment Is not Verified"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PublishBlog(request):
    userid = request.data["user"]
    
    # Get the BlogSettings instance for the given user
    blogsetting = BlogSettings.objects.get(user=userid)

    # Serialize the blog settings
    blogSettingSerial = BlogSettingSerializer(blogsetting)

    # Create a blog serializer with the data from the request
    serializer = BlogSerializer(data=request.data)
    
    # Check if payment is verified
    if blogSettingSerial.data["paymentVerified"]:
        if serializer.is_valid():
            # Save the blog, associating it with the current authenticated user
            blogdata = serializer.save(user=request.user)
            
            if blogdata:
                # Increment the blog count
                blogCountIncrease = blogsetting.blogcount + 1  # Access blogcount from the model instance
                
                # Update the BlogSettings instance with the new blog count
                settingsJson = {"blogcount": blogCountIncrease}

                # Serialize the updated BlogSettings instance with partial updates
                settingSerializer = BlogSettingSerializer(blogsetting, data=settingsJson, partial=True)

                if settingSerializer.is_valid():
                    settingSerializer.save()  # Save the updated blog count
                    return Response({
                        'msg': 'Blog created successfully',
                        'blog': serializer.data,
                    }, status=201)
                
        return Response(serializer.errors)
    
    return Response({"msg": "Payment is not verified"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddComment(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        # blogValata = serializer.save()
        serializer.save(commenter=request.user)

        return Response({
            'msg': 'Blog created successfully',
            'blog': serializer.data,
        }, status=201)
    
    return Response(serializer.errors)

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def BlogList(request):
   
    blg = Blog.objects.all()

    serializer = BlogSerializer(blg, many = True, fields=['id', 'title', 'description', 'blogimg', 'user'])

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SingleBlog(request, pk=None):
   
    # singleUserData = User.objects.get(id=pk)
    blog = get_object_or_404(Blog.objects.prefetch_related('comments'), id=pk)  # Prefetch blogs for the user
    serializer = BlogSerializer(blog)

    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def UpdateBlog(request, pk=None):
    id = pk
    blogVal = Blog.objects.get(pk=id)

    serializer = BlogSerializer(blogVal, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Blog Data Updated'})
    
    return Response(serializer.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteBlog(request, pk=None):
    try:
        blog = Blog.objects.get(pk=pk)  # Retrieve the blog instance
        if blog.blogimg:
            if default_storage.exists(blog.blogimg.path):
                default_storage.delete(blog.blogimg.path) 
        blog.delete()  # Delete the instance
        return Response({'msg': 'Blog deleted successfully'}, status=200)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)
