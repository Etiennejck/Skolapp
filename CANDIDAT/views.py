from django.contrib import admin, sessions
from django.contrib.auth.models import User
from django.contrib.messages.storage import session
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from CANDIDAT.forms import ParentIncriptionForm, StudentIncriptionForm
from CANDIDAT.models import Student


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
        if form.is_valid():
            form.save()

        else:
            form = ParentIncriptionForm()
    return render(request, 'CANDIDAT/inscriptionParent.html', {'form': form})

