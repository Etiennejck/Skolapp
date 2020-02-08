from django.urls import path
from django.conf.urls import url
from CANDIDAT import views
from CANDIDAT.views import list_Students, details_Students, update_Student

urlpatterns = [
    url(r'^inscriptionSchool', views.inscriptionSchool, name='inscriptionSchool'),
    url(r'^inscriptionParent/', views.inscriptionParent, name='inscriptionParent'),
    url(r'^remaining_class', views.NbrRestant, name='remaining_class'),
    path('ListStudents/', list_Students.as_view(), name='listeStudents'),
    url(r'^DetailStudents/(?P<id>\d+)/$', details_Students.as_view(), name='DetailStudents'),
    url(r'^UpdateStudent/(?P<id>\d+)/$', update_Student.as_view(), name='UpdateStudent'),
]