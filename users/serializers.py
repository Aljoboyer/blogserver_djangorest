from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'about', 'profileImg']
    def create(self, validated_data):
            password = validated_data.pop('password')  # Remove password from validated data
            user = User(**validated_data)
            user.set_password(password)  # Hash the password using the set_password method in the model
            user.save()
            return user