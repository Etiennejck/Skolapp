from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


def validate_email(value):
    if value != r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)":
        raise EmailValidator(message='veuillez saisir une addresse valide')

def validate_integer(value):
    if value < 1 or value > 6:
        raise ValidationError(
            ('%(value)s doit etre modifié'),
            params={'value':value}
        )

class Parent(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField(verbose_name="date de naissance")
    Nationalite = models.CharField(verbose_name="Nationalité", max_length=300, null=True)
    rue = models.CharField(verbose_name="Rue, numero",max_length=70)
    cp = models.IntegerField(verbose_name="Code postal")
    ville = models.CharField(max_length=100)
    Telephone = PhoneNumberField(null=True, region='BE')
    mail = models.EmailField(help_text='addresse email',validators=[validate_email])
    dateInscription = models.DateField(verbose_name="date d'inscription", auto_now_add=True)

    class Meta:
        ordering = ['-dateInscription']

    def __str__(self):
        return "Nom: {} Prenom: {} Date d'inscription: {} id= {}".format(self.nom, self.prenom, self.dateInscription, self.id)


class Student(models.Model):
    SECTION = [('Maternelle 1','Maternelle 1'), ('Maternelle 2','Maternelle 2'),('Maternelle 3','Maternelle 3'), ('Primaire','Primaire')]
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=2)
    dateNaissance = models.DateField()
    Nationalite = models.CharField(verbose_name="Nationalité", max_length=300, null=True)
    section = models.CharField(max_length=50, choices=SECTION, default=False)
    ClassePrecedente = models.IntegerField(verbose_name="Classe précédente", default=1, validators=[validate_integer])
    langueMaternelle = models.CharField(verbose_name="Langue maternelle", max_length=50)
    repasChaud = models.BooleanField(verbose_name="Repas chaud", default=False)
    XtraScolaire = models.BooleanField(verbose_name="Sortie extra scolaire", default=False)
    AccordPedagogique = models.BooleanField(verbose_name="Accord pédagogique", default=False)
    AccordImage = models.BooleanField(verbose_name="Accord diffusion image", default=False)
    GardeParental = models.CharField(verbose_name="Garde parental", max_length=50)
    class_journal = models.TextField(verbose_name='notes des parents', null=True)
    parents_id = models.ForeignKey('Parent', on_delete=models.CASCADE, default=False, verbose_name='Parent')
    presence = models.BooleanField(default=False, null=True)


    def __str__(self):
        return "id: {} nom: {}, prenom: {}, section {}, fils de {} - {} id= {} present: {}".format(self.id ,self.nom, self.prenom, self.section,self.parents_id.nom, self.parents_id.prenom, self.parents_id.id, self.presence)

    def get_absolute_url(self):
        return reverse('DetailStudents', kwargs={'id':self.id})

    class Meta:
        ordering = ['section']





