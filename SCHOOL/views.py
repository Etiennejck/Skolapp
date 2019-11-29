from datetime import datetime
from CANDIDAT.models import Parent, Student
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate, login
from django.contrib import messages


def Home(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Home.html', {'dateDuJour': dateDuJour,'heure': heure})

def welcom(request):
    return render(request, 'SCHOOL/Welcom.html')


def dashboardProf(request):
    students = Student.objects.all()
    return render(request, 'SCHOOL/dashboardProf.html', {'students': students})


def LoginParent(request, **kwargs):
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboardProf')
    else:
        messages.error(request, 'your email or password is not correct')
    return render(request, 'SCHOOL/loginParent.html')
