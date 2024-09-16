from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.AllUsers),
    path('create_user/', views.Create_User),
    path('login/', views.Login),
]
