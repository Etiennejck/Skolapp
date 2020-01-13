from django.contrib import admin, sessions
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from CANDIDAT import models
from CANDIDAT.forms import ParentIncriptionForm, StudentIncriptionForm
from CANDIDAT.models import Student, Parent
import pandas as pd



def inscriptionSchool(request):
    form2 = StudentIncriptionForm(request.POST or None)

    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
            return redirect('inscriptionParent')
        else:
            form2 = StudentIncriptionForm()
    return render(request, 'CANDIDAT/inscriptionSchool.html', {'form2': form2})


def inscriptionParent(request):
    form = ParentIncriptionForm(request.POST or None)
    if request.method == 'POST':
        password = request.POST['pswd']
        username = request.POST['username']
        if form.is_valid():
            form.save()
            user = User.objects.create_user(username=form['mail'].value(),email=form['mail'].value(), password=password)
            return redirect('welcom')
        else:
            form = ParentIncriptionForm()
    return render(request, 'CANDIDAT/inscriptionParent.html', {'form': form})

