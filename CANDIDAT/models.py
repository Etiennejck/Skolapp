from django.db import models
from INSCRIPTION.models import Inscription

class Student(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=2)
    dateNaissance = models.DateField()
    ClassePrecedente = models.IntegerField(verbose_name="Classe précédente", default=0)
    langueMaternelle = models.CharField(verbose_name="Langue maternelle", max_length=50)
    repasChaud = models.BooleanField(verbose_name="Repas chaud", default=False)
    XtraScolaire = models.BooleanField(verbose_name="Sortie extra scolaire", default=False)
    AccordPedagogique = models.BooleanField(verbose_name="Accord pédagogique", default=False)
    AccordImage = models.BooleanField(verbose_name="Accord diffusion image", default=False)
    GardeParental = models.CharField(verbose_name="Garde parental", max_length=50)
    parentFK = models.OneToOneField("Parent", on_delete=models.CASCADE)


class Parent(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField(verbose_name="date de naissance")
    rue = models.CharField(verbose_name="Rue, numero",max_length=70)
    cp = models.IntegerField(verbose_name="Code postal")
    ville = models.CharField(max_length=100)
    mail = models.EmailField()
    dateInscription = models.DateField(verbose_name="date d'inscription", auto_now_add=True)
    inscriptionFK = models.ForeignKey(Inscription, on_delete=models.CASCADE)


