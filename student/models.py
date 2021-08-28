from django.db import models
from accounts.models import User
from course_coordinator.models import Classes
# Create your models here.

class TimeTable(models.Model):
    student_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(to=Classes, on_delete=models.CASCADE, related_name="timetable")
    