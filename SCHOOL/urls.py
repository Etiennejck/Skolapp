from django.conf.urls import url
from django.urls import path

from SCHOOL import views
from SCHOOL.views import JournalDeClasseView

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^welcom', views.welcom, name='welcom'),
    url(r'^dashboardProf', views.dashboardProf, name='dashboardProf'),
    url(r'^LoginParent', views.LoginParent,name='LoginParent'),
    url(r'^LogOut_view', views.LogOut_view,name='LogoutView'),
    path('JDCView/', JournalDeClasseView.as_view()),
]