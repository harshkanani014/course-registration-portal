from django.urls import path
from .views import *


urlpatterns = [
    # User API endpoints
    path('get-timetable', GetTimeTable.as_view()), # Get User API
    path('register-course', AddTimeTable.as_view()),
    path('delete-course/<int:id>', DeleteCourse.as_view()),

    path('get-available-classes', AllCourses.as_view())
]