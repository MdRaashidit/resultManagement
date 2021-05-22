
from examination.views import create_student,marks,semester
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', semester, name='index'),
    path('signup', create_student, name='signup'),
    path('marks', marks, name='marks'),
    # path('sem',semester, name='sem'),
    path('accounts/', include('django.contrib.auth.urls')),
]
