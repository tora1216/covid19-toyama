# coding:utf-8

import json
import codecs
import re
import requests
from bs4 import BeautifulSoup

# 現時点のデータを取得
data = json.load(codecs.open('../data/news.json', 'r', 'utf-8'))

# 富山県HPから最新の情報を取得
url = "http://www.pref.toyama.jp/sections/1118/virus/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.content, "html.parser")

news = []

table = soup.find("table")
update_date = re.search(r"(\d+)年(\d+)月(\d+)日", table.find('td').text)
date = update_date.group(1)+"-"+update_date.group(2).zfill(2)+"-"+update_date.group(3).zfill(2)
for a in table.findAll('a'):
  url = a.attrs['href']
  text = a.text
  news.append({"date": date, "url": url, "text": text})

data["newsItems"]=news

# news.json上書き
df_result = codecs.open('../data/news.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
