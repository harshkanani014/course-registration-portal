from enum import unique
from os import name
from django.db import models
from django.db.models.base import Model

# Create your models here.

# Model for courses available
class Courses(models.Model):
    course_code = models.TextField(unique=True)
    course_name = models.TextField(unique=True, max_length=10000)

    def __str__(self):
        return self.course_name


# Model for location of building in which class is going to be conducted
class Location(models.Model):
    building_name = models.TextField(max_length=5000)
    latitude = models.DecimalField(max_digits=100, decimal_places=50, default=0)
    longitude = models.DecimalField(max_digits=100, decimal_places=50, default=0)

    def __str__(self):
        return self.building_name


# Model to add classes
class Classes(models.Model):
    course_code = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    faculty = models.TextField(max_length=50000)
    day = models.TextField(default='')
    time = models.TimeField(null=True)
    building = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    students_registered = models.IntegerField(default=0)

    class Meta:
        unique_together = ('course_code', 'faculty', 'day', 'time',)

