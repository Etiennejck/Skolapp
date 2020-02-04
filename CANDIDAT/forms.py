from django.forms import ModelForm, CharField, Textarea, Select, ChoiceField, forms, ModelChoiceField
from CANDIDAT.models import Parent, Student
from django.core.exceptions import NON_FIELD_ERRORS, FieldDoesNotExist
from phonenumber_field.modelfields import PhoneNumberField

class ParentIncriptionForm(ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
        labels={
            'Telephone': ('Numero de téléphone'),
        }
        help_texts = {
            'Telephone': ('Commencer le numero par +32'),
        }
        error_messages = {
            'Telephone': {
                'PhoneNumberField':('Pas oublier de ne pas mettre le 0 apres +32'),

            }
        }


class StudentIncriptionForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


