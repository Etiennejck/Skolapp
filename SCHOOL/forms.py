from django import forms
from CANDIDAT.models import Student

class Check_presence(forms.Form):
    students = Student.objects.all()

