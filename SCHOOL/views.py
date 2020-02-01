from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from SCHOOL.models import Professor
from CANDIDAT.models import Parent, Student
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from SCHOOL.models import ClassRoom


def Home(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Home.html', {'dateDuJour': dateDuJour,'heure': heure})

def welcom(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Welcom.html', {'dateDuJour': dateDuJour,'heure': heure})


def dashboardProf(request):
    if request.user.is_authenticated:
        liste_de_présence = []
        if request.method == 'POST':
            presence = request.POST['presence']
            liste_de_présence.append(presence)
        user = request.user
        students = Student.objects.all()
        student_in_the_class = [i for i in Student.objects.all() if i.section == 'Maternelle 2']
        MathNbr = len(student_in_the_class)
        professors = [i.prenom for i in Professor.objects.all()]


        return render(request, 'SCHOOL/dashboardProf.html', {'students': students, 'user':user, 'student_in_the_class':student_in_the_class, 'MathNbr':MathNbr, 'Professor': professors})
    else:
        messages.info(request, 'Vous n\'est pas loger' )
        return redirect('welcom')

def dashboardParent(request):
    if request.user.is_authenticated:
        user = request.user
        students = Student.objects.all()
        return render(request, 'SCHOOL/dashboardParent.html', {'students': students, 'user':user})
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
            return redirect('dashboardParent')
        else:
            messages.error(request, 'your email or password is not correct')
            return redirect('welcom')
    return render(request, 'SCHOOL/loginParent.html')

def LogOut_view(request):
    logout(request)
    return render(request, 'SCHOOL/Welcom.html')

class JournalDeClasseView(ListView):
    model = Student #Definie le model de la base de données que l'on va utilisé c'est = à (queryset= model.object.all())
    context_object_name = 'Etudiant' #permet de changer le nom de la variable à utilisé dans le gabarit
    template_name = 'SCHOOL/JDCView.html'
    note_de_compmortement = {}
    devoir = []

    def post(self, request, **kwargs):
        if request.method == 'POST':
            noteComportement = request


def communicationSchool(request):
    return render(request, 'SCHOOL/communicationSchool.html')