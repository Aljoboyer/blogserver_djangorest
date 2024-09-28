from django.db import models
from django.conf import settings  # Import the custom user model
import uuid

# Create your models here.
class BlogSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blogcount = models.IntegerField()
    paymentVerified = models.BooleanField()
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='settinguser')
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updatedAt = models.DateTimeField(auto_now=True)