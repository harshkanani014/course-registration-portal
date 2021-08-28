from django.urls import path
from .views import *


urlpatterns = [
    # User API endpoints
    path('add-user', AddUserView.as_view()), # Add User API
    path('get-user', GetUser.as_view()), # Get User API

    path('add-course', AddCourse.as_view()), # Add Course
    path('get-course', GetCourse.as_view()), # Get Course

    path('add-classes', AddClass.as_view()),
    path('get-classes', GetClass.as_view()),

    path('add-location', AddLocation.as_view()),
    path('get-location', GetLocation.as_view()),

    path('get-course-location/<int:id>', GetCourseLocation.as_view())
]