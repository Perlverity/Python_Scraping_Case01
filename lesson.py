import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
URL = 'http://www.python.org'

r = requests.get(URL, headers=headers)

print(r.url)
print(r.status_code)
