from django.urls import path
from django.conf.urls import url
from CANDIDAT import views

urlpatterns = [
    url(r'^inscriptionSchool', views.inscriptionSchool, name='inscriptionSchool'),
    url(r'^inscriptionParent/(\d+)/$', views.inscriptionParent, name='inscriptionParent'),
]