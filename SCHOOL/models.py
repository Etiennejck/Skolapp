from django.db import models
from django.urls import reverse
from django.utils import timezone



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
    number = models.IntegerField(verbose_name="nombre de classe")
    nombrePlaces = models.IntegerField(verbose_name="capacitée de la classe", null=True)

    def __str__(self):
        return 'Section: {} , nombre de classe: {} , nombre de place restante: {}'.format(self.sectionClass, self.number, self.nombrePlaces)

class ClassSection(models.Model):
    sectionRoom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE)
    intitule = models.CharField(verbose_name='Intitulé', max_length=20, null=True)
    prof = models.ForeignKey('Professor', on_delete=models.CASCADE)
    currentYears = models.ForeignKey('Years', on_delete=models.CASCADE)


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
    def __str__(self):
        return "{}, {}, {}, {}".format(self.nom, self.prenom, self.statut, self.sectionProf)


class School_subjects(models.Model):
    nom = models.CharField(max_length=100)


class Teaches(models.Model):
    school_subjectFK = models.ForeignKey(School_subjects, on_delete=models.CASCADE, default=False)
    professorFK = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroomFK = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)


class Inscription(models.Model):
    dateInscription = models.DateField(verbose_name="date d'inscription")
    parents = models.ForeignKey('CANDIDAT.Parent', on_delete=models.CASCADE)


class Years(models.Model):
    schoolYear = models.DateTimeField(verbose_name="année scolaire", default=timezone.now)#affiche par defaut la date courante

    def __str__(self):
        return "Année scolaire en cours {} ".format(self.schoolYear)

class Journal_de_classe(models.Model):

    annee_scolaire = models.ForeignKey('Years', on_delete=models.CASCADE, auto_created=True)
    date_du_jour = models.DateField(verbose_name="date du jour", auto_now_add=True)
    professeur = models.ForeignKey('Professor', on_delete=models.CASCADE)
    student_id = models.ForeignKey('CANDIDAT.Student', on_delete=models.CASCADE)
    intitule_du_devoir = models.CharField(max_length=50,verbose_name='intitule du devoir')
    detail_du_devoir = models.TextField(verbose_name='devoir', null=True)
    note_de_comportement = models.TextField(verbose_name='note de comportement', null=True)

    def get_absolute_url(self):
        return reverse('Journal_de_classe-detail', kwargs={'id':self.id})
