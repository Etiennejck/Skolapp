from django.db import models
from django.utils import timezone
from CANDIDAT.models import Parent


class School (models.Model):
    nom = models.CharField(max_length=100)
    status = models.BooleanField()
    rue = models.CharField(max_length=100)
    cp = models.IntegerField(verbose_name="Code postal")
    ville = models.CharField(max_length=100)
    inscriptionFK = models.ForeignKey("Inscription", on_delete=models.CASCADE)
    classroomFK = models.ForeignKey("ClassRoom", on_delete=models.CASCADE)


class ClassRoom(models.Model):
    sectionClass = models.CharField(verbose_name="Section", max_length=50)
    number = models.IntegerField(verbose_name="numero de la classe")


class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    dateNaissance = models.DateField()
    mail = models.EmailField()
    dateInscription = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Professor(Personne):
    sectionProf = models.CharField(max_length=100)


class School_subjects(models.Model):
    nom = models.CharField(max_length=100)


class Enseigne(models.Model):
    school_subjectFK = models.ForeignKey(School_subjects, on_delete=models.CASCADE)
    professorFK = models.ForeignKey(Professor, on_delete=models.CASCADE)


class Teaches(models.Model):
    professorFK = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroomFK = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)


class QuarterTeaches(models.Model):
    teachesFK = models.ForeignKey(Teaches, on_delete=models.CASCADE)
    quarter = models.ForeignKey("Quarter", on_delete=models.CASCADE)


class Quarter(models.Model):
    quarterNr = models.IntegerField(verbose_name="Trimestre numero")


class QuarterClass(models.Model):
    classRooms = models.ForeignKey("ClassRoom", on_delete=models.CASCADE)
    quarters = models.ForeignKey(Quarter, on_delete=models.CASCADE)


class Inscription(models.Model):
    dateInscription = models.DateField(verbose_name="date d'inscription")
    parents = models.ForeignKey(Parent, on_delete=models.CASCADE)


class Years(models.Model):
    schoolYear = models.DateTimeField(verbose_name="année scolaire", default=timezone.now)#affiche par defaut la date courante
    inscriptionFK = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    quarterFK = models.ForeignKey(Quarter, on_delete=models.CASCADE)