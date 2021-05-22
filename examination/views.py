from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Result, Course, Grade, Semester
from django.contrib.auth.decorators import user_passes_test


# @login_required
# def index(request):
#     results = Result.objects.filter(student=request.user)
#     context = {"results": results}
#     return render(request, "index.html", context)


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
        return redirect('index')
    return render(request, 'signup.html')

@user_passes_test(lambda u: u.is_superuser)
def marks(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        semester = request.POST.get("semester")
        subjects = request.POST.getlist("course")
        grades = request.POST.getlist("grade")
        l = len(grades)
        student = User.objects.get(username=rollno)
        semester = Semester.objects.get(value=semester)
        for i in range(l):
            subject = subjects[i]
            grade = Grade.objects.get(value=grades[i])
            course = Course.objects.get(title__iexact=subject)
            mark = Result(student=student, subject=course,
                          semester=semester, grade=grade)
            mark.save()

    context = {"courses": Course.objects.all(), "student": User.objects.filter(
        is_superuser=False), "semester": Semester.objects.all(), "grades": Grade.objects.all()}
    return render(request, 'admin.html', context)

@login_required
def semester(request):
    sems = None
    if request.method == 'POST':
        sem = Semester.objects.get(value=request.POST.get('sem'))
        sems = Result.objects.filter(semester=sem, student=request.user)
    context = {"sems": sems, "semester": Semester.objects.all()}
    return render(request, "index.html", context)
