from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

from .views import profile_view, RegisterView

urlpatterns = [

    path("", views.index, name='home'),
    path("demand/", views.demand, name='demand'),
    path("geography/", views.geography, name='geography'),
    path("skills/", views.skills, name='skills'),
    path("latest-vacancies/", views.latestVacancies, name='latest-vacancies'),
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)