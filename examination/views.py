from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


<<<<<<< HEAD
def home(request):
    return render
=======
def index(request):
    return render(request, "index.html")


def create_student(request):
    if request.method == 'POST':
        rollno = request.POST.get("rollno")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        encrypted_password = make_password(password)
        user = User(
            username=rollno,
            password=encrypted_password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
    return render(request, 'signup.html')


# def login_user(request):
#     rollno = request.POST.get("rollno")
#     password = request.POST.get("password")
#     user = authenticate(request, username=rollno, password=password)
#     return render(request,'login.html')
>>>>>>> 575b1f7 (Signup)
