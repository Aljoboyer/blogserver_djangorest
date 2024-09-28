from django.contrib import admin
from . models import BlogSettings

# Register your models here.
@admin.register(BlogSettings)
class BlogSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'blogcount', 'paymentVerified', 'user', 'createdAt', 'updatedAt']