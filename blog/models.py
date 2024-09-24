from django.db import models
import uuid
from django.conf import settings  # Import the custom user model

# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    description = models.TextField()
    blogimg = models.ImageField(upload_to='blog_images/', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')  # Foreign key to custom user
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updatedAt = models.DateTimeField(auto_now=True)    # Automatically updated when modified

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commenttext = models.TextField()
    comments = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commenter')
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updatedAt = models.DateTimeField(auto_now=True) 