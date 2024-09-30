from django.urls import path
from . import views

urlpatterns = [
    path('paymentverify/', views.PaymentVerfying),
]
