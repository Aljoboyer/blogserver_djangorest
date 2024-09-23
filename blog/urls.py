from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.PublishBlog),
    path('addcomment/', views.AddComment),
    path('single/<uuid:pk>', views.SingleBlog),
]
