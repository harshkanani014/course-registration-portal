from django.shortcuts import render

# Create your views here.
def login_template(request):
    return render(request, 'login.html')

def otp_verify_template(request):
    return render(request, 'verify_otp.html')
