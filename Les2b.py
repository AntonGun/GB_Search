#https://russia.superjob.ru/vakansii/data-scientist.html?click_from=facet
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup as bs

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"}

link = 'https://russia.superjob.ru/vakansii/data-scientist.html?click_from=facet'

vac = 'data-scientist'

params = {'text': 'Data scientist',
          'area': 1,
          'experience': 'doesNotMatter',
          'order_by': 'relevance',
          'search_period': 0,
          'items_on_page': 2,
          'page': 2}

response = requests.get(link, headers=headers)
soup = bs(response.text, 'html.parser')

vacancies = soup.find_all('div', {'class': 'f-test-search-result-item'})

vac_name = vacancies[0].find('span', {'class': '-gENC _1TcZY Bbtm8'})
vac_title = vac_name.getText()
print(vac_title)

vac_list = []
for vacancy in vacancies:
    vac_dict = {}

    vac_name = vacancy.find('span', {'class': '-gENC _1TcZY Bbtm8'})
    vac_title = vac_name.getText()
    vac_dict['Title'] = vac_title

    vac_link = vacancy.find('a')['href']
    vac_dict['Link'] = 'https://russia.superjob.ru/' + vac_link

    vac_salary = vacancy.find('span', {'class': '_2eYAG -gENC _1TcZY mO3i1 dAWx1'})
    vac_salary = vac_salary.getText()
    vac_dict['Salary'] = vac_salary

    if vac_salary is None:
        max_salary = None
        min_salary = None
        currency = None
    else:
        vac_salary = vac_salary.getText()
        if vac_salary.startswith('до'):
            max_salary = int("".join([s for s in vac_salary.split() if s.isdigit()]))
            min_salary = None
            currency = vac_salary.split()[-1]
        elif vac_salary.startswith('от'):
            max_salary = None
            min_salary = int("".join([s for s in vac_salary.split() if s.isdigit()]))
            currency = vac_salary.split()[-1]
        else:
            max_salary = int("".join([s for s in vac_salary.split('–')[1] if s.isdigit()]))
            min_salary = int("".join([s for s in vac_salary.split('–')[0] if s.isdigit()]))
            currency = vac_salary.split()[-1]

    vac_dict['Max Salary'] = max_salary
    vac_dict['Min Salary'] = min_salary
    vac_dict['Currency'] = currency

    if 'https:' in link:
        vac_site = link[8:].partition('/')[0]  # https://
    else:
        vac_site = link[7:].partition('/')[0]  # http://
    vac_dict['Website'] = vac_site

    vac_region = vacancy.find('span', {'class': 'f-test-text-company-item-location _4uUzb _1TcZY mO3i1 dAWx1'})
    vac_dict['Region'] = vac_region.getText()

    vac_list.append(vac_dict)


print(len(vac_list))
pprint(vac_list)