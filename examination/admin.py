from django.contrib import admin
from .models import Course,Result

admin.site.register([Course,Result])