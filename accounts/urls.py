from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('login', LoginView.as_view()), # API for login
    path('verify-otp', OtpVerify.as_view()), # API endpoint to verify OTP
    path('resend-otp', resend_otp), # API to resend OTP
    path('logout', LogoutView.as_view()), # API for logout
]