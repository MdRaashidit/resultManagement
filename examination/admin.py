from django.contrib import admin
from .models import Course,Result,Grade,Semester

admin.site.register([Course,Result,Grade,Semester])