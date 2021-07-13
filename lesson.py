import requests
from bs4 import BeautifulSoup

import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
URL = 'http://www.python.org'

r = requests.get(URL, headers=headers, timeout=3)

soup = BeautifulSoup(r.content, 'lxml')
post = soup.find('div', class_='blog-widget')


for i, li in enumerate(post.find_all('li')):
    print('='*30, i, '='*30)
    print(li.find('a').text)
    print(li.find('time').text)