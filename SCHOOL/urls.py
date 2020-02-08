from django.conf.urls import url
from django.urls import path
from django.views.generic import *
from SCHOOL import views
from SCHOOL.views import JournalDeClasseView, ClassRoom,  Journal_de_classeCreate, \
    Journal_de_classeUpdate, Journal_de_classeDelete, Journal_de_classeDetail

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^welcom', views.welcom, name='welcom'),
    url(r'^dashboardProf', views.dashboardProf, name='dashboardProf'),
    url(r'^LoginParent', views.LoginParent,name='LoginParent'),
    url(r'^LogOut_view', views.LogOut_view,name='LogoutView'),
    path('JDCView/', JournalDeClasseView.as_view(), name='Journaldeclasse'),
    url(r'^dashboardParent', views.dashboardParent, name='dashboardParent'),
    url(r'^communicationSchool', views.communicationSchool, name='communicationSchool'),
    path('Journal_de_classeAdd', Journal_de_classeCreate.as_view(), name='Journal_de_classeAdd'),
    path('Journal_de_classeUpdate/<int:id>/', Journal_de_classeUpdate.as_view(), name='Journal_de_classe-update'),
    path('Journal_de_classeDetail/<int:id>/', Journal_de_classeDetail.as_view(), name='Journal_de_classe-detail'),
    path('Journal_de_classeDelete/<int:id>/', Journal_de_classeDelete.as_view(), name='Journal_de_classe-delete'),
]