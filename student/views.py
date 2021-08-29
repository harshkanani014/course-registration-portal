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


from accounts.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *
import jwt
from rest_framework.views import APIView
from .models import *



# Create your views here.

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


# API to register course  for course registration portal
# API Endpoint : register-course
# Request : POST
class AddTimeTable(APIView):
    serializer_class = TimeTableSerializer
    def post(self, request):
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        
        # Permission : Only course student can register course
        if user.is_student:
            serializer = TimeTableSerializer(data=request.data)
            class_id = request.data['class_id']
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "error": serializer.errors,
                    "message": "",
                    "data": user.email
                })

            serializer.save()
            get_class = Classes.objects.get(id=class_id)
            get_class.students_registered += 1
            get_class.save()

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


# API to get timtable for course registration portal
# API Endpoint : get-timetable
# Request : GET
class GetTimeTable(APIView):
    def get(self, request):
        # verify token for authorization
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()  
        except:
            return payload
            
        all_timetable = TimeTable.objects.filter(student_id=user.id)
        serializer = GetTimeTableSerializer(all_timetable, many=True)
        return Response({
            'success': True,
            'message':'',
            'data':serializer.data
        })


# API For deleting course from time table
# endpoint : delete-course/id (timetable course id)
# request : DELETE
class DeleteCourse(APIView):
    def delete(self, request, id):
        # verify token
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()
        except:
            return payload
        course = TimeTable.objects.get(id=id)
        if user.is_student:
            course.delete()
            return Response({
                'success': True,
                'message': 'Course deleted from your time table',
                })
        else:
            return Response({
                'success': False,
                'message': 'You are not allowed to delete Course',
            })


# API to get available course for student registration portal
# API Endpoint : get-available-course
# Request : GET
class AllCourses(APIView):
    def get(self, request):
        # verify token for authorization
        payload = verify_token(request)
        try:
            user = User.objects.filter(id=payload['id']).first()  
        except:
            return payload
        
        
        # Queries to exclude registered courses and slot clash from all available classes
        all_timetable = TimeTable.objects.filter(student_id=user)
        all_classes = Classes.objects.all().exclude(id__in=all_timetable.values_list('class_id')).exclude(day__in=all_timetable.values_list('class_id__day'))
        all_classes = all_classes.exclude(time__in=all_timetable.values_list('class_id__time'))
        
        serializer = GetClassSerializer(all_classes, many=True)
        return Response({
            'success': True,
            'message':'',
            'data':serializer.data
        })

