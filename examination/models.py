from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    credit = models.PositiveIntegerField()
    semester = models.CharField(max_length=30)





