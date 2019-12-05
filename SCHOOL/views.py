from datetime import datetime

from django.contrib.auth.decorators import login_required

from CANDIDAT.models import Parent, Student
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Home(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Home.html', {'dateDuJour': dateDuJour,'heure': heure})

def welcom(request):
    return render(request, 'SCHOOL/Welcom.html')


def dashboardProf(request):
    if request.user.is_authenticated:
        students = Student.objects.all()
        return render(request, 'SCHOOL/dashboardProf.html', {'students': students})
    else:
        messages.info(request, 'Vous n\'est pas loger' )
        return redirect('welcom')



def LoginParent(request, **kwargs):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardProf')
        else:
            messages.error(request, 'your email or password is not correct')
            return redirect('welcom')
    return render(request, 'SCHOOL/loginParent.html')

def LogOut_view(request):
    logout(request)
    return render(request, 'SCHOOL/Welcom.html')