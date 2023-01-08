from msilib.schema import Environment

from django.shortcuts import render
from jinja2 import FileSystemLoader
from xlsx2html import xlsx2html


def index(request):
    return render(request, 'main/home.html')

def demand(request):
    # env = Environment(loader=FileSystemLoader('C:/Users/anony/app/analytics/main/templates/main'))
    # template = env.get_template("demand.html")
    #
    # out1 = xlsx2html('C:/Users/anony/app/analytics/main/static/img/report.xlsx', sheet='Статистика по годам')
    # out1.seek(0)
    # code1 = out1.read()
    # out2 = xlsx2html('C:/Users/anony/app/analytics/main/static/img/report.xlsx', sheet='Статистика по городам')
    # out2.seek(0)
    # code2 = out2.read()
    vac_name = "web-разработчик"
    # pdf_template = template.render({'name_vacancy': vac_name, 'table1': "dfdfd"})

    return render(request, 'main/demand.html', {'name_vacancy': vac_name})

def geography(request):
    return render(request, 'main/geography.html')

def skills(request):
    return render(request, 'main/skills.html')

def latestVacancies(request):
    return render(request, 'main/latest-vacancies.html')
