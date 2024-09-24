from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from datetime import datetime

# Custom user manager to handle user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('about', {"hhdf":"kfhksdf"})

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # Use a larger field for hashed passwords
    about = models.JSONField()
    profileImg = models.ImageField(upload_to='profile_images/', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

   # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updatedAt = models.DateTimeField(auto_now=True)     # Automatically updated when modified
    
    USERNAME_FIELD = 'email'  # Email will be used for authentication
    REQUIRED_FIELDS = ['name']  # Fields that are required besides the email

    objects = CustomUserManager()  # Use the custom user manager

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
