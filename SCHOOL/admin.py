from django.contrib import admin

from CANDIDAT.models import Student, Parent
from SCHOOL.models import *

admin.site.register(ClassRoom)
admin.site.register(Teaches)
admin.site.register(Professor)
admin.site.register(Years)
admin.site.register(Inscription)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(ClassSection)
admin.site.register(School_subjects)


