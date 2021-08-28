from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Abstract User model re-used to add extra fields
class User(AbstractUser):
    name = models.TextField(max_length=100)
    registration_number = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=100)
    is_course_coordinator = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD = 'registration_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# model for saving otp of user and its expiry
class loginDetails(models.Model):
    email = models.EmailField(unique=True)
    otp = models.TextField()
    exp = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.email
