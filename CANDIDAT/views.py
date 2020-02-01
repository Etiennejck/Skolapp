from datetime import date

from django.contrib import admin, sessions, messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from SCHOOL.models import ClassRoom
from CANDIDAT.forms import ParentIncriptionForm, StudentIncriptionForm
from CANDIDAT.models import Student




def inscriptionSchool(request):
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

            return redirect('inscriptionParent')
        else:
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
                return redirect('welcom')
            else:
                form = ParentIncriptionForm()
        except:
            messages.error(request, 'cette addresse mail existe déjà !!!')

    return render(request, 'CANDIDAT/inscriptionParent.html', {'form': form, 'placefree':placefree, 'students':studs[-3:]})


def NbrRestant(request):
    placefree = ClassRoom.objects.all()

    return render(request, 'CANDIDAT/remaining_class.html',{'placefree': placefree})

