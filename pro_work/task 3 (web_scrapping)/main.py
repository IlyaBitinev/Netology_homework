import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import json

HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()


def cook_soup():
    response = requests.get(HOST, headers=get_headers()).text
    soup = BeautifulSoup(response, features='lxml')
    return soup


keywords = ["Django", "Flask"]
cursor = 0
all_vacancys = {}
articles_all = cook_soup().find(class_='vacancy-serp-content')
article_tags = articles_all.find_all(class_="vacancy-serp-item__layout")

for article in article_tags:
    vacancy_name = article.find('a', class_='serp-item__title')
    link = vacancy_name['href']
    fool_vacancy = requests.get(link, headers=get_headers()).text
    soup_vacancy = BeautifulSoup(fool_vacancy, features='lxml')
    detail_vacancy = soup_vacancy.find(class_='g-user-content')
    salary_vacancy = soup_vacancy.find(class_='bloko-header-section-2 bloko-header-section-2_lite')
    detail_vacancy_txt = detail_vacancy.text
    for item in keywords:
        if item in detail_vacancy_txt:
            name_company = article.find('a', class_='bloko-link bloko-link_kind-tertiary')
            city = article.find('div', class_="bloko-text", attrs={'data-qa': 'vacancy-serp__vacancy-address'})
            jobs = []
            jobs.append(
                {'Ссылка': link,
                 'Вилка зп': salary_vacancy.text.replace('\xa0', ' '),
                 'Название компании': name_company.text,
                 'Город': city.text})
            cursor += 1
            count = (f' Найдена вакансия {cursor}')
            all_vacancys[count] = jobs

pprint(all_vacancys)

with open('new_find_vacancy.json', 'w', encoding='utf-8') as nv:
    json.dump(all_vacancys, nv, ensure_ascii=False, indent=4)
