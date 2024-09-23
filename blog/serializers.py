from rest_framework import serializers
from . models import Blog, Comment
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# User Serializer (to return user data)
class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'profileImg']  # Customize fields as needed


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    commenter = UserSerializer(read_only=True) 


    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  
    user = UserSerializer(read_only=True) 

    class Meta:
        model = Blog
        fields = '__all__'
