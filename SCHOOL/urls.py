from django.conf.urls import url

from SCHOOL import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^welcom', views.welcom, name='welcom'),
    url(r'^dashboardProf', views.dashboardProf, name='dashboardProf'),
    url(r'^LoginParent', views.LoginParent,name='LoginParent'),
]