from django.urls import path
from django.conf.urls import url
from CANDIDAT import views

urlpatterns = [
    url(r'^inscriptionSchool', views.inscriptionSchool, name='inscriptionSchool'),
    url(r'^inscriptionParent/', views.inscriptionParent, name='inscriptionParent'),
    url(r'^remaining_class', views.NbrRestant, name='remaining_class'),
]