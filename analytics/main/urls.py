
from django.urls import path
from . import views

urlpatterns = [

    path("home/", views.index, name='home'),
path("demand/", views.demand, name='demand'),
path("geography/", views.geography, name='geography'),
path("skills/", views.skills, name='skills'),
path("latest-vacancies/", views.latestVacancies, name='latest-vacancies'),

    path('index/', views.index1)


]
