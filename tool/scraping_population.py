import datetime
import pandas as pd
import json

# 現在日時
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# モバイル空間統計より最新データ取得
url = 'https://mobaku.jp/covid-19/download/%E5%A2%97%E6%B8%9B%E7%8E%87%E4%B8%80%E8%A6%A7.csv'
df = pd.read_csv(url, encoding='SHIFT-JIS')
df = df.iloc[176:180, -7:]

df = df.to_dict(orient='list')
datasets = []
for key, value in df.items(): 
    datasets.append({
        "label": key,
        "data": value
    })

data = {
    "date": dt,
    "datasets": datasets,
    "labels": [
        "感染拡大前比",
        "緊急事態宣言前比",
        "前年同月比",
        "前日比"
    ],
    "base_period": "2020年1月18日~2020年2月14日"
}

f = open('../data/population.json', 'w', encoding='utf-8')
json.dump(data, f, ensure_ascii=False, indent=4)
