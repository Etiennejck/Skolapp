from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=2)
    dateNaissance = models.DateField()
    Nationalite = models.CharField(verbose_name="Nationalité", max_length=300, null=True)
    ClassePrecedente = models.IntegerField(verbose_name="Classe précédente", default=0)
    langueMaternelle = models.CharField(verbose_name="Langue maternelle", max_length=50)
    repasChaud = models.BooleanField(verbose_name="Repas chaud", default=False)
    XtraScolaire = models.BooleanField(verbose_name="Sortie extra scolaire", default=False)
    AccordPedagogique = models.BooleanField(verbose_name="Accord pédagogique", default=False)
    AccordImage = models.BooleanField(verbose_name="Accord diffusion image", default=False)
    GardeParental = models.CharField(verbose_name="Garde parental", max_length=50)

    def __str__(self):
        return "nom: {}, prenom: {}".format(self.nom, self.prenom)

class Parent(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField(verbose_name="date de naissance")
    Nationalite = models.CharField(verbose_name="Nationalité", max_length=300, null=True)
    rue = models.CharField(verbose_name="Rue, numero",max_length=70)
    cp = models.IntegerField(verbose_name="Code postal")
    ville = models.CharField(max_length=100)
    Telephone = PhoneNumberField(null=True)
    mail = models.EmailField()
    dateInscription = models.DateField(verbose_name="date d'inscription", auto_now_add=True)
    def __str__(self):
        return "Nom: {} Prenom: {} Date d'inscription: {}".format(self.nom, self.prenom, self.dateInscription)



