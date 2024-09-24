from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.PublishBlog),
    path('addcomment/', views.AddComment),
    path('list/', views.BlogList),
    path('single/<uuid:pk>', views.SingleBlog),
    path('update/<uuid:pk>', views.UpdateBlog),
    path('delete/<uuid:pk>', views.DeleteBlog),
]
