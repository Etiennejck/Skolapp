from django.db import models
from django.utils import timezone
from SCHOOL.models import School


class Inscription(models.Model):
    dateInscription = models.DateField(verbose_name="date d'inscription")




class Years(models.Model):
    schoolYear = models.DateTimeField(verbose_name="année scolaire", default=timezone.now)#affiche par defaut la date courante
    inscriptionFK = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    quarterFK = models.ForeignKey("Quarter", on_delete=models.CASCADE)


class Quarter(models.Model):
    quarterNr = models.IntegerField(verbose_name="Trimestre numero", max_length=2)


