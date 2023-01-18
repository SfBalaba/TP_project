import json
import os
import re
from typing import List, Dict
import pandas as pd
import requests
import concurrent.futures
import openpyxl
from django.shortcuts import render
from jinja2 import FileSystemLoader
from xlsx2html import xlsx2html
import xlrd
from django.conf import settings


def data_from_xlsx(path):
    vac_name = "web-разработчик"
    path = os.path.join(settings.MEDIA_ROOT, str(path).replace('/', '\\'))

    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    print(ws)
    excel_data = list()
    for row in range(ws.nrows):
        row_data = list()
        for col in range(ws.ncols):
            cell_value = ws.cell(row, col).value

            value = int(cell_value)\
                if ( len(str(cell_value))!=0 and str(cell_value)[-1] == '0') else cell_value
            row_data.append(value)
        excel_data.append(row_data)
    return excel_data, vac_name

url = "https://api.hh.ru/vacancies"

def execute_vacancies(vacancies: List[Dict[str, str]] or List[Dict[Dict[str, str], str]]) -> (List[List[str]]):
    """ формирует дату для создания итогового датафрейма
    оставляет только нужные поля: название, город, вилка оклада, дата публиукации вакансии
    Args:
        vacancies: список словарей выгруженных api содержащие информацию по вакасии
    Returns: список вакансий c зарплатами
    """
    return [
        [
            vacancy['id'],
            vacancy["name"],
            vacancy["area"]["name"],
            vacancy["salary"]["from"],
            vacancy["salary"]["to"],
            vacancy["salary"]["currency"],
            vacancy["published_at"],
        ]
        for vacancy in vacancies
        if vacancy["salary"]
    ]

def get_vacancies_items(params: dict) -> (List[Dict[str, str]] or List[Dict[Dict[str, str], str]]):
    """ поулчает json данные о вакансии по заданынм параметрам
    Args:
        params: параметры для запроса
    Returns: данные по вакансиям
    """
    return requests.get(url, params).json()["items"]


def get_latest_vac():

    pd.set_option('expand_frame_repr', False)

    pages_count = 20
    params1 = [
        dict(
            specialization=1,
            date_from="2022-12-15T00:00:00",
            date_to="2022-12-15T12:00:00",
            per_page=100,
            page=i,
        )
        for i in range(pages_count)
    ]

    params2 = [
        dict(
            specialization=1,
            date_from="2022-12-15T12:00:00",
            date_to="2022-12-16T00:00:00",
            per_page=100,
            page=i,
        )
        for i in range(pages_count)
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = list(executor.map(get_vacancies_items, params1 + params2))
        response = list(executor.map(execute_vacancies, result))
        result = pd.concat(
            [
                pd.DataFrame(
                    el,
                    columns=[
                        'id',
                        "name",
                        "area_name",
                        "salary_from",
                        "salary_to",
                        "salary_currency",
                        "published_at"
                    ]
                )
                for el in response
            ]
        )
    vacancy_name = ['web-develop', 'веб-разработчик', 'web-разработчик', 'web programmer', 'web программист','битрикс',
                    'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик',
                    'cms разработчик',
                    'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer',
                    'cms developer',
                    'wordpress developer', 'wp developer', 'joomla developer']
    flag = True
    for vac in vacancy_name:
        if (flag):
            df2 = result[result['name'].str.contains(vac, flags=re.IGNORECASE,
                                                     regex=True)]
        else:
            new = result[result['name'].str.contains(vac, flags=re.IGNORECASE,
                                                     regex=True)]
            df2 = pd.concat([df2, new], axis=0, ignore_index=True)
        flag = False
    df2 = df2.head(10)
    for i in range(df2.shape[0]):
        new_get = requests.get(f"https://api.hh.ru/vacancies/{df2.loc[[i], ['id']].values[0][0]}").json()
        df2.loc[[i], ['company']] = new_get["employer"]["name"]
        df2.loc[[i], ['description']] = new_get['description']
        if (len(new_get['key_skills']) != 0):
            df2.loc[[i], ['key_skills']] = ", ".join([x['name'] for x in new_get['key_skills']])
        else:
            df2.loc[[i], ['key_skills']] = ""

    df2["published_at"] = df2["published_at"].apply(lambda x: x[:10])
    df2['salary'] = df2[['salary_from', 'salary_to']].mean(axis=1)
    df2 = df2.dropna(subset=['salary_from', 'salary_to'], how='all').reset_index(drop=True)
    df2 = df2.loc[df2['salary_currency'] == 'RUR']
    df2 = df2.drop(["salary_from", "salary_to"], axis=1)
    df2 = df2.drop(['id'], axis=1)
    json_records = df2.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    return data
