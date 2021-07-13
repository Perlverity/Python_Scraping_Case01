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

# Requestsライブラリ
## サイトへのアクセス方法
1. requests.get(url):指定したURLにアクセスする
2. requests.get(url, params=params):パラメータを指定してURLにアクセスする
3. requests.get(url, headers=headers):ヘッダーを指定してURLにアクセスする

## アクセス結果の確認
1. r.text:レスポンスで受け取ったデータをテキスト(str型)で取得する
2. r.content:レスポンスで受け取ったデータをバイナリ(byte型)で取得する
3. r.raise_for_status():ステータスコードに応じてエラーを発生させる