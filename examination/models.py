from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=30)
    grade = models.CharField(max_length=1)
