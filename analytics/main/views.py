

import openpyxl
from django.shortcuts import render
from jinja2 import FileSystemLoader
from xlsx2html import xlsx2html


def index(request):
    return render(request, 'main/home.html')

def insert_table(file_name, sheet_name):

    wb = openpyxl.load_workbook('C:/Users/anony/app/analytics/main/static/img/report.xlsx')
    worksheet = wb["Статистика по годам"]
    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)

def demand(request):
    vac_name = "web-разработчик"
    wb = openpyxl.load_workbook('C:/Users/anony/app/analytics/main/static/img/report.xlsx')
    worksheet = wb["Статистика по годам"]
    print(worksheet)

    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    return render(request, 'main/demand.html', {'name_vacancy': vac_name, "excel_data": excel_data})

def geography(request):
    vac_name = "web-разработчик"
    wb = openpyxl.load_workbook('C:/Users/anony/app/analytics/main/static/img/report.xlsx')
    worksheet = wb["Статистика по городам"]
    print(worksheet)

    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    return render(request, 'main/geography.html', {'name_vacancy': vac_name, "excel_data": excel_data})

def skills(request):
    vac_name = "web-разработчик"
    wb = openpyxl.load_workbook('C:/Users/anony/app/analytics/main/static/img/skills_stat.xlsx')
    worksheet = wb["Навыки"]

    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    return render(request, 'main/skills.html', {'name_vacancy': vac_name, "excel_data": excel_data})

def latestVacancies(request):
    return render(request, 'main/latest-vacancies.html')

def index1(request):
    return render(request, 'main/index.html')