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


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that controls 
    which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    commenter = UserSerializer(read_only=True) 


    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(DynamicFieldsModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  
    user = UserSerializer(read_only=True) 

    class Meta:
        model = Blog
        fields = '__all__'
