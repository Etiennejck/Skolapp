from datetime import datetime
from CANDIDAT.models import Parent, Student
from django.shortcuts import render
from django.utils.datetime_safe import date


def Home(request):
    dateDuJour = date.today()
    heure = datetime.now()


    return render(request, 'SCHOOL/Home.html', {'dateDuJour': dateDuJour,'heure': heure})

def dashboardProf(request):
    students = Student.objects.all()
    return render(request, 'SCHOOL/dashboardProf.html', {'students': students})