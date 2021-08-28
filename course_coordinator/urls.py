from django.urls import path
from .views import *


urlpatterns = [
    # User API endpoints
    path('add-user', AddUserView.as_view()),
    path('get-user', GetUser.as_view()),
    path('add-course', AddCourse.as_view()),
    path('get-course', GetCourse.as_view())
]