from datetime import date

from django.contrib import admin, sessions, messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from SCHOOL.models import ClassRoom
from CANDIDAT.forms import ParentIncriptionForm, StudentIncriptionForm, JournalDeClasssForm
from CANDIDAT.models import Student, Parent




def inscriptionSchool(request):
    lastParent = Parent.objects.last()
    form2 = StudentIncriptionForm(request.POST or None)

    allSection = ClassRoom.objects.all()
    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
            stud = form2['nom'].value()
            sect = form2['section'].value()
            SectionSave = ClassRoom.objects.get(sectionClass=sect)
            SectionSave.nombrePlaces -= 1
            SectionSave.save()
            return redirect('welcom')
        else:
            messages.error(request, "Oups! un problème est survenu")
            form2 = StudentIncriptionForm()
    return render(request, 'CANDIDAT/inscriptionSchool.html', {'form2': form2,'test':allSection})


def inscriptionParent(request):
    studs = [i.nom+" "+i.prenom for i in Student.objects.all()]
    try:
        placefree = [i for i in ClassRoom.objects.all().order_by('sectionClass') if i.nombrePlaces > 0]

    except:
        messages.error(request, "Il ne sera plus possible d'inscrire d'enfants pour le moment ")

    form = ParentIncriptionForm(request.POST or None)
    if request.method == 'POST':
        password = request.POST['pswd']
        username = request.POST['username']
        try:
            if form.is_valid():
                form.save()
                user = User.objects.create_user(username=form['mail'].value(),email=form['mail'].value(), password=password)
                #cls = ClassRoom.objects.filter(sectionClass=username).filter(number=)
                return redirect('inscriptionSchool')
            else:
                messages.error(request, "Oups! un problème est survenu")
                form = ParentIncriptionForm()
        except:
            messages.error(request, 'cette addresse mail existe déjà !!!')

    return render(request, 'CANDIDAT/inscriptionParent.html', {'form': form, 'placefree':placefree, 'students':studs[-3:]})


def NbrRestant(request):
    placefree = ClassRoom.objects.all()

    return render(request, 'CANDIDAT/remaining_class.html',{'placefree': placefree})


# vue basée sur des classes

class list_Students(ListView):
    model = Student
    template_name = 'SCHOOL/ListStudents.html'
    queryset = Student.objects.all()


class details_Students(DetailView):
    model = Student
    template_name = 'SCHOOL/DetailStudents.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

class update_Student(UpdateView):
    template_name = "CANDIDAT/UpdateStudent.html"
    form_class = StudentIncriptionForm #reference au modelForm
    queryset = Student.objects.all()

#passe l'id du model en parametre
    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)
#Valide le formulaire
    def form_valid(self, form):
        return super().form_valid(form)


