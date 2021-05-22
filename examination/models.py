from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Semester(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value


class Grade(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value


class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,  on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
