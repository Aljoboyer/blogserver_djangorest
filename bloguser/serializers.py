from rest_framework import serializers
from . models import User
from blog.serializers import BlogSerializer

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    blogs = BlogSerializer(many=True, read_only=True)  # Include the related blogs

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'name', 'email', 'phone', 'password', 'about', 'profileImg', 'blogs']  # Only include these fields
        extra_kwargs = {
            'password': {'write_only': True}  # Exclude password from the response but allow it during creation
        }
    def create(self, validated_data):
            password = validated_data.pop('password')  # Remove password from validated data
            user = User(**validated_data)
            user.set_password(password)  # Hash the password using the set_password method in the model
            user.save()
            return user