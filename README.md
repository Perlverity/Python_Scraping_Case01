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
pip install lxml
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

# Requestsライブラリ(①データの収集 - クローリング)
## サイトへのアクセス方法
1. requests.get(url):指定したURLにアクセスする
2. requests.get(url, params=params):パラメータを指定してURLにアクセスする
3. requests.get(url, headers=headers):ヘッダーを指定してURLにアクセスする

## アクセス結果の確認
1. r.text:レスポンスで受け取ったデータをテキスト(str型)で取得する
2. r.content:レスポンスで受け取ったデータをバイナリ(byte型)で取得する
3. r.raise_for_status():ステータスコードに応じてエラーを発生させる

# BeautifulSoupライブラリ(②データの解析 - スクレイピング - lxml)
## HTML解析器
1. Python標準のHTML解析器(=ライブラリをインストール必要がない)
2. lxml --> 高速の動作をする。ただし、ライブラリのインストールが必要。
3. html5lib --> HTML5を生成する。ただし、処理が遅い。

## HTMLの解析方法
1. BeautifulSoup(r.content, 'lxml'):HTMLを解析する

## 解析したHTMLからタグを抽出する方法
1. find('タグ名'):該当するタグを持つ最初の要素を取得する
2. find(id='id名'):該当するidを持つ要素を取得する
3. find(class_='class名'):該当するclassを持つ最初の要素を取得する
4. find(text=re.compile('text')):指定したテキストを持つ最初の要素を習得する

## タグから情報を抽出する方法
1. find().text:指定した要素からテキストを取得する
2. find().get('href):指定した要素からhrefの値を取得する