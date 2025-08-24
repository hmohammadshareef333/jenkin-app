from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class studentform(models.Model):
    ename=models.CharField(max_length=20)
    rollno=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    mobileno=models.CharField(max_length=20)
    image=models.ImageField(default='default.jpg',upload_to='updates')