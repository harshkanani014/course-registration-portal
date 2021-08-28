"""
organization : motorQ
created_by : Harsh Kanani
last_updated_by : Harsh Kanani
last_updated : '28-08-2021'
Code-format-standard : PEP-8
Status : {
    "API": done, 
    "backend testing : done, 
    "documentation: done,
    "postman API added" : done,
    }
"""

from django.shortcuts import render
from django.http.response import HttpResponse
from accounts.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *
import jwt
import math
from django.db.models import Q
from rest_framework.views import APIView
from .models import *
import io
from rest_framework.parsers import MultiPartParser, FormParser

# Function to get serializer errors 
def get_error(serializerErr):

    err = ''
    
    for i in serializerErr:
        err = serializerErr[i][0]
        break    
        
    return err


# Function to verify JWT token
def verify_token(request):

    try:
        if not (request.headers['Authorization'] == "null"):
            token = request.headers['Authorization']
    except:
        if not (request.COOKIES.get('token') == "null"):
            token = request.COOKIES.get('token')
            
    else:
        context = {
            "success": False,
            "error": "Not Authorized",
            "message": "",
        }
        payload = JsonResponse(context)
        
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except:
        context = {
            "success": False,
            "error": "UnAuthenticated",
            "message": "",
        }
        payload = JsonResponse(context)
    
    return payload


# API to add users for course registration portal
# API Endpoint : add-user
# request : POST
class AddUserView(APIView):
    def post(self, request):
        #verify token i.e checks user is authenticated or not
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
       # checks user is course co-ordinator or not
        if user.is_course_coordinator:            
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                "success":False,
                "error":get_error(serializer.errors),
                "message":"",
                "data": user.email
                })

            serializer.save()
            return Response({
                "success":True,
                "error":"",
                "message":"User added successfully",
                "data":serializer.data
                })

        else:
            return Response({
                "success":False,
                "error":"Not authorized to access this page",
                "message":"",
                "data":{
                    "email":user.email
                }
            })


# API to get Users for course registration portal
# API Endpoint : get-user
# Request :GET
class GetUser(APIView):
    def get(self, request):
        # verify token for authorization
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()  
        except:
            return payload
        
        # Query : To get all users registered
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response({
            'success': True,
            'message':'',
            'data':serializer.data
        })


# API to add users for course registration portal
# API Endpoint : add-course
# Request : POST
class AddCourse(APIView):
    serializer_class = CourseSerializer
    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        # Permission : Only course co-ordinator can add course
        if user.is_course_coordinator:
            serializer = CourseSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "error": get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "Course added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add Course",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


# API to get courses for course registration portal
# API Endpoint : get-course
# Request : GET
class GetCourse(APIView):
    def get(self, request):
        # verify token for authorization
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()  
        except:
            return payload
            
        all_courses = Courses.objects.all()
        serializer = CourseSerializer(all_courses, many=True)
        return Response({
            'success': True,
            'message':'',
            'data':serializer.data
        })


# API to add class for course registration portal
# API Endpoint : add-class
# Request : POST
class AddClass(APIView):
    serializer_class = ClassSerializer
    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        # Permission : Only course co-ordinator can add course
        if user.is_course_coordinator:
            serializer = ClassSerializer(data=request.data)
            
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "error": get_error(serializer.errors),
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            return Response({
                "success": True,
                "error": "",
                "message": "Class added successfully",
                "data": serializer.data
            })
        else:
            return Response({
                "success": False,
                "error": "Not authorized to Add Class",
                "message": "",
                "data": {
                    "email": user.email
                }
            })


# API to get class for course registration portal
# API Endpoint : get-class
# Request : GET
class GetClass(APIView):
    def get(self, request):
        # verify token for authorization
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()  
        except:
            return payload
            
        all_class = ClassSerializer.objects.all()
        serializer = ClassSerializer(all_class, many=True)
        return Response({
            'success': True,
            'message':'',
            'data':serializer.data
        })
    


