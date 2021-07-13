import requests
from bs4 import BeautifulSoup
from time import sleep

import re
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
URL = 'http://www.python.org'

r = requests.get(URL, headers=headers, timeout=3)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')

d_list = []

for li in post.find_all('li'):

    post_url = li.find('a').get('href')

    sleep(2)

    post_r = requests.get(post_url)
    post_soup = BeautifulSoup(post_r.content, 'lxml')
    post_h2 = [h2.text for h2 in post_soup.find_all('h2')]

    d = {
        'title': li.find('a').text,
        'url': li.find('a').get('href'),
        'date': li.find('time').text
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
print(df)

df.to_csv('python_web_posts.csv', index=None, encoding='utf-8-sig')
df.to_excel('python_web_posts.xlsx', index=None, encoding='utf-8-sig')