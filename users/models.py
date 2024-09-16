from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    about = models.JSONField()
    profileImg =  models.ImageField(upload_to='profile_images/', null= True)

    def set_password(self, raw_password):
       self.password = make_password(raw_password)