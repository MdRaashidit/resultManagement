
from examination.views import index,create_student,marks,semester
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup', create_student, name='signup'),
    path('marks', marks, name='marks'),
    path('sem',semester, name='sem'),
    path('accounts/', include('django.contrib.auth.urls')),
]
