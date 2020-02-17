from datetime import datetime

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from SCHOOL.models import Professor, Journal_de_classe, ClassSection
from CANDIDAT.models import Parent, Student
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from CANDIDAT.forms import JournalDeClasssForm
from django.contrib.auth.decorators import login_required
from SCHOOL.models import ClassRoom
from django.contrib.sessions.models import Session


def Home(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Home.html', {'dateDuJour': dateDuJour,'heure': heure})

def welcom(request):
    dateDuJour = date.today()
    heure = datetime.now()
    return render(request, 'SCHOOL/Welcom.html', {'dateDuJour': dateDuJour,'heure': heure})

def loginProfessor(request):
    return render(request, 'SCHOOL/loginProfessor.html' )


def dashboardProf(request):
    if request.user.is_authenticated and request.user.groups.exists():
        students = Student.objects.all()

        user = request.user
        profSection = [i.professeur.sectionProf for i in Journal_de_classe.objects.all() if i.professeur.mail == user.email ]
        student_in_the_class = Student.objects.all().filter(journal_de_classe__professeur__mail=user.email)
        MathNbr = len(student_in_the_class)
        professors = [i.sectionProf for i in Professor.objects.all().filter(mail=user.email)]
        class_De = ClassSection.objects.all().filter(prof__mail=user.email)
        JDC_ID = Journal_de_classe.objects.all()
        contextdash =  {
            'students': students,
            'user':user,
            'student_in_the_class':student_in_the_class,
            'MathNbr':MathNbr,
            'Professor': " ".join(professors),
            'class_De':class_De,
            'JDC_ID':JDC_ID,
            'profSection':profSection,
        }
        return render(request, 'SCHOOL/dashboardProf.html',contextdash)
    else:
        messages.info(request, 'Vous n\'est pas loger' )
        return redirect('LoginProfessor')

def dashboardParent(request):
    if request.user.is_authenticated and not request.user.groups.exists():
        user = request.user
        jdcStudent = Journal_de_classe.objects.all().filter(student_id__parents_id__mail=user.email)
        print(user.email, user.id)
        if request.method == 'POST':
            message = request.POST['message']
            Student.objects.filter(parents_id__mail=user.email).update(class_journal=message)
        return render(request, 'SCHOOL/dashboardParent.html', {'user':user,'jdcStudent':jdcStudent})
    else:
        messages.info(request, 'Vous n\'est pas encore inscrit ', )
        return redirect('welcom')

def presence(request):
    students = Student.objects.filter(journal_de_classe__professeur__mail=request.user.email)
    if request.method == 'POST':
        presenceQuest = request.POST['presenceState']
        print(presenceQuest)
        studId = students.filter(id=presenceQuest)
        print(studId)
        if studId.filter(presence=True):
            studId.update(presence=False)
        elif studId.filter(presence=False):
            studId.update(presence=True)
        return redirect('dashboardProf')

    return render(request, 'SCHOOL/presence.html', {'presenceUser':students})



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


def LoginProfessor(request, **kwargs):
    username = None
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardProf')
        else:
            messages.error(request, 'your email or password is not correct')
            return redirect('welcom')
    return render(request, 'SCHOOL/LoginProfessor.html', {'username':username})

def LogOut_view(request):
    logout(request)
    return render(request, 'SCHOOL/Welcom.html')

def LogOutProf_view(request):
    logout(request)
    return render(request, 'SCHOOL/loginProfessor.html')

class JournalDeClasseView(ListView):
    model = Journal_de_classe #Definie le model de la base de données que l'on va utilisé c'est = à (queryset= model.object.all())
    template_name = 'SCHOOL/JDCView.html'
    queryset = Journal_de_classe.objects.all()
    paginate_by = 30

class Journal_de_classeCreate(CreateView):
    template_name = 'SCHOOL/Journal_de_classeAdd.html'
    form_class = JournalDeClasssForm
    queryset = Journal_de_classe.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class Journal_de_classeDetail(DetailView):
    template_name = 'SCHOOL/Journal_de_classeDetail.html'
    model = Journal_de_classe

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Journal_de_classe, id=id)

class Journal_de_classeUpdate(UpdateView):
    template_name = 'SCHOOL/Journal_de_classeAdd.html'
    form_class = JournalDeClasssForm
    queryset = Journal_de_classe.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    studId = [i.id for i in Journal_de_classe.objects.all()]

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Journal_de_classe, id=id)



class Journal_de_classeDelete(DeleteView):
    model = Journal_de_classe
    success_url = reverse_lazy('Journaldeclasse')

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(Journal_de_classe, id=id)






def communicationSchool(request):
    return render(request, 'SCHOOL/communicationSchool.html')