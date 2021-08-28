"""
organization : motorQ
created_by : Harsh Kanani
last_updated_by : Harsh Kanani
last_updated : '28-08-2021'
Code-format-standard : PEP-8

"""


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
import jwt, datetime
import random
import time
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render

# Function for sending OTP via email
def send_email(otp, email_1):
    
    email = EmailMultiAlternatives('2FA OTP for COURSE REGISTRATION portal', ' Your OTP is :' + otp)
    email.to = [email_1]
    email.send()

# API to verify user login
# API Endpoint : /login
# request : POST
class LoginView(APIView):
    def post(self, request):
        registration_number = request.data['registration_number']
        password = request.data['password']
        user = User.objects.filter(registration_number=registration_number).first()
        
        if user is None:
            context = {

                "success":False,
                "error":"User not found",
                "message":"",
                "data":
                {
                }
            }
            return JsonResponse(context)

        if not user.check_password(password):
            context = {
                "success":False,
                "error":"In-correct password",
                "message":"",
                "data":
                {
                }
            }
            return JsonResponse(context)
        
        email = user.email
        otp = random.randint(1000, 9999)      
        print("otp :", otp)
        
        # try:
        #     send_email(str(otp), email)
        # except:
        #     context = {
        #         "success":False,
        #         "error":"Unable to send otp to given E-Mail",
        #         "message":"",
        #         "data":
        #         {
        #             "email":email,
        #             "is_active":False
        #         }
        #     }
        #     return JsonResponse(context)

        expire_at = time.time() + 300
        new_login = loginDetails()
        try:
            new_login.email = email
            new_login.otp = otp
            new_login.exp = expire_at
            new_login.is_active = True
            new_login.save()
        except:
            new_login = loginDetails.objects.get(email=email)
            new_login.otp = otp
            new_login.exp = expire_at
            new_login.is_active = True
            new_login.save()

        context = {
            "success":True,
            "error":"",
            "message":"OTP sent successully",
            "data":
            {
                "email":email,
                "is_active":True
            }
        }
        return JsonResponse(context)


# API for checking otp and verifying it
# API endpoint : verify-otp
# Request : POST
class OtpVerify(APIView):
    def post(self, request):
        email = request.data['email']
        otp = request.data['otp']
        current_req = loginDetails.objects.get(email=email)

        if current_req.is_active==True:
                if time.time() > float(current_req.exp):
                    
                    context = {
                    "success":False,
                    "error":"OTP was expired!",
                    "message":"",
                    "data":
                        {
                        "email":email,
                        }
                    }
                    return Response(context)

                elif int(current_req.otp)==int(otp):
                    
                    user = User.objects.get(email=email)
                    current_req.is_active = False
                    current_req.save()

                    payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=500),
                    'iat': datetime.datetime.utcnow()
                    }

                    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8') #generating token
                    response = Response()
                    response.set_cookie(key='token', value=token, httponly=True)
                   
                    response.data = {
                        "success":True,
                        "error":"",
                        "message":"User login successfully",
                        "data":
                            {
                            "id":user.id,
                            "registration_number": user.registration_number,
                            "email":user.email,
                            "is_student":user.is_student,
                            "is_course_coordinator": user.is_course_coordinator,
                            "token":token,
                           }
                        }
                    return response
                else:
                    context = {
                        "success":False,
                        "error":"OTP was wrong",
                        "message":"",
                        "data":
                        {
                            "email":email
                        }
                    }
                    return Response(context)
        else:
            context = {
                "success":False,
                "error":"no data",
                "message":"",
                "data":""
            }
            return Response(context)


# API for resending otp to user after expiring.
# API Endpoint : /resend-otp
# Request : GET            
@api_view(["POST"])
def resend_otp(request):
    email = request.data['email']
    current_req = loginDetails.objects.get(email=email)
    if current_req.is_active:
        # checks if OTP expired or not
        if time.time()> float(current_req.exp):
            otp = random.randint(1000,9999)
            print("otp", otp)
            try:
                send_email(str(otp), email)
            except:
                context = {
                    "success":False,
                    "error":"Unable to send otp to given E-Mail",
                    "message":"",
                    "data":
                    {
                        "email":email,
                        "is_active":False
                    }
                }
                return JsonResponse(context)

            expire_at = time.time() + 300
            current_req.otp = otp
            current_req.exp = expire_at
            current_req.save()
            
            context = {
                    "success":True,
                    "error":"",
                    "message":"OTP resend successfully",
                    "data":
                    {
                            "email":email
                    }
                }
            return Response(context)
        else:
            context = {
                    "success":False,
                    "error":"OTP already exist",
                    "message":"",
                    "data":
                    {
                            "email":email
                    }
                }
            return Response(context)
    else:
        context = {
                "success":False,
                "error":"no data",
                "message":"",
                "data":""
            }
        return Response(context)


# API for logout
# API Endpoint : /logout
# Request : GET
class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('token') #delete the token
        response.data = {
            "error":"",
            'message': "Logout success"
        }
        return response


      