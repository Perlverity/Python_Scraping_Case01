from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0112M%2C0113M%2C010401S%2C010402S%2C010404S&so=50&tp=1&page={}&usrclk_searchList=PC-logoutJobSearchList_searchResultHeaderArea_pagination_prev'
d_list = []

for i in range(1, 5):
    URL = BASE_URL.format(i)
    sleep(3)

    # URL = 'https://doda.jp/DodaFront/View/JobSearchList.action?ss=1&pr=13&pic=1&ds=0&oc=0112M%2C0113M%2C010401S%2C010402S%2C010404S&so=50&tp=1'
    r = requests.get(URL, timeout=3)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')
    companies = soup.find_all('div', class_='layoutList02')

    for i, company in enumerate(companies):
        print('='*30, i, '='*30)
        company_name = company.find('span', class_='company').text
        page_url = company.find('a', class_='btnJob03').get('href')

        page_url = page_url.replace('-tab__pr', '-tab__jd')
        sleep(3)

        page_r = requests.get(page_url, timeout=3)
        page_r.raise_for_status()

        page_soup = BeautifulSoup(page_r.content, 'lxml')

        table = page_soup.find('table', id='company_profile_table')
        company_url = table.find('a')
        if company_url:
            company_url = company_url.get('href')

        d_list.append({
            'company_name': company_name,
            'company_url': company_url,
        })

        df = pd.DataFrame(d_list)
        df.to_csv('company_list.csv', index=None, encoding='utf-8-sig')
