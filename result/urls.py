
from examination.views import index,create_student
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('examination.urls')),
=======
    path('', index, name='index'),
    path('signup', create_student, name='signup'),
>>>>>>> 575b1f7 (Signup)
]
