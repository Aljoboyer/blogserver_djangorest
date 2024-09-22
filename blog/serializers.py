from rest_framework import serializers
from . models import Blog

class BlogSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'