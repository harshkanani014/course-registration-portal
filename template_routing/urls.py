from django.urls import path
from .views import *

urlpatterns = [
    path('', login_template, name="login_view"),
    path('verify-otp', otp_verify_template, name="verify_otp")
]
 
 
 
 