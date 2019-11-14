from django.contrib import admin, sessions
from django.shortcuts import render
from CANDIDAT.forms import ParentIncriptionForm, StudentIncriptionForm


def inscriptionSchool(request):
    form = ParentIncriptionForm(request.POST or None)
    form2 = StudentIncriptionForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid() and form2.is_valid():
            form.save() and form2.save()
    return render(request, 'CANDIDAT/inscriptionSchool.html', {'form':form, 'form2': form2})

