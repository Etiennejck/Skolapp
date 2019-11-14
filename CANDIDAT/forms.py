from django.forms import ModelForm, forms
from django import forms
from CANDIDAT.models import Parent, Student


class ParentIncriptionForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class StudentIncriptionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'