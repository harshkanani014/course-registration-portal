from django.urls import path
from .views import *


urlpatterns = [
    # User API endpoints
    path('add-user', AddUserView.as_view()), # Add User API
    path('get-user', GetUser.as_view()), # Get User API

    path('add-course', AddCourse.as_view()), # Add Course
    path('get-course', GetCourse.as_view()), # Get Course

    path('add-class', AddClass.as_view()),
    path('get-class', GetClass.as_view())
]