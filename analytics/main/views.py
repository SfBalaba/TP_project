from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from pyexpat.errors import messages

from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Demand, Home, Geography, Skills
from .services import data_from_xlsx, get_latest_vac


def index(request):
    data = Home.objects.last()
    return render(request, 'main/home.html', {"data": data})

def demand(request):
    data = Demand.objects.last()
    path = data.excel
    excel_data, vac_name = data_from_xlsx(path)
    context = {'name_vacancy': vac_name, "data": data, "excel_data": excel_data[1:], "heads": excel_data[0]}
    return render(request, 'main/demand.html', context=context)


def geography(request):
    data = Geography.objects.last()
    path = data.excel
    excel_data, vac_name = data_from_xlsx(path)
    context = {'name_vacancy': vac_name, "data": data, "excel_data": excel_data[1:], "heads": excel_data[0]}
    return render(request, 'main/geography.html', context=context)


def skills(request):
    data = Skills.objects.last()
    path = data.excel
    excel_data, vac_name = data_from_xlsx(path)
    context = {'name_vacancy': vac_name, "data": data, "excel_data": excel_data[1:], "heads": excel_data[0]}
    return render(request, 'main/skills.html', context=context)


def latestVacancies(request):
    data = get_latest_vac()
    context = {"data": data}
    return render(request, 'main/latest-vacancies.html', context=context)

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)