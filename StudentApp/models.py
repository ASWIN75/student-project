from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    joining_date = models.DateField(null=True)
    qualification = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=255, null=True)