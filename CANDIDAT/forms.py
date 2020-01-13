from django.forms import ModelForm, CharField, Textarea, Select, ChoiceField, forms
from CANDIDAT.models import Parent, Student


class ParentIncriptionForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'


class StudentIncriptionForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'