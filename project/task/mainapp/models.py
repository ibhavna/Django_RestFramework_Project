from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)



class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=100,unique=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
