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