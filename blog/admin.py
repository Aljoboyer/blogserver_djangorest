from django.contrib import admin
from . models import Blog, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'blogimg', 'user', 'createdAt', 'updatedAt']

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'commenttext', 'comments', 'commenter']