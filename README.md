# Python_Scraping_Case01

1. データの収集(クローリング)
> Webサイトにアクセスしてデータ(HTML)を収集する
2. データの抽出(スクレイピング)
> 収集したHTMLを解析して必要なデータを抽出する
3. データの保存
> 抽出したデータを保存する

# github python
```
pip install GitPython
```

# Library List
|  Library  | ①データ収集 |  ②データの抽出   |  ③データの保存   |
|:---:|:---:|:---:|:---:|
|  Requests   |  ○  |     |     |
|  BeautifulSoup   |     |   ○  |     |
|  Selenium   |  ○  |  ○   |     |
|  Pandas   |     |     |   ○  |

# User-Agentの偽装
```
headers = {
    'User-Agent': ''
}
```