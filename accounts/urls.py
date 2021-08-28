from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view()),
    path('verify-otp', OtpVerify.as_view()),
    path('resend-otp', resend_otp),
    path('logout', LogoutView.as_view()),
]