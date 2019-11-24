from django.conf.urls import url

from SCHOOL import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^dashboardProf', views.dashboardProf)
]