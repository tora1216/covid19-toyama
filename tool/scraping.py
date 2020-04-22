# coding:utf-8

import json
import codecs
import datetime
import re
import mojimoji
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 現時点のデータを取得
data = json.load(codecs.open('../data/data.json', 'r', 'utf-8'))

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
data["lastUpdate"] = dt_now

# 富山県HPから最新の情報を取得
url = "http://www.pref.toyama.jp/cms_sec/1205/kj00021798.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.content, "html.parser")

# 要約テキストを取得
main_list = soup.find("div", id="main")
text = main_list.find("p").text
summary_text = re.search(r"(.+)例（入院中.+(.+)例、退院(.+)例、死亡(.+)例）", text)

# 一覧エクセルを取得
file_list = soup.find("div", id="file")
link = file_list.find("a", text="富山県内における新型コロナウイルス感染症の発生状況一覧").get("href")
df_kanjya = pd.read_excel(link, skiprows=2)

# エクセル内データを定義書準拠形式に変換
df_kanjya.rename(columns={"県番号": "No"}, inplace=True)
df_kanjya.rename(columns={"検査結果判明日": "判明日"}, inplace=True)
df_kanjya["判明日"] = df_kanjya["判明日"].apply(
    lambda date: pd.to_datetime(date, unit="D", origin=pd.Timestamp("1899/12/30")).strftime("%Y-%m-%d")
)
df_kanjya['性別'] = df_kanjya["性別"].replace("男", "男性").replace("女", "女性")
df_kanjya['年代'] = df_kanjya["年代"].replace("90代", "90歳以上").replace("90代以上", "90歳以上")

# 検査陽性者の状況
data["main_summary"] = {
    "date": dt_now,
    "children": [{
        "attr": "陽性患者数",
        "value": int(mojimoji.zen_to_han(summary_text.group(1))),
        "children": [{
            "attr": "入院",
            "value": int(mojimoji.zen_to_han(summary_text.group(2))),
            "children": [{
                "attr": "無症状・軽症・中等症",
                "value": data["main_summary"]["children"][0]["children"][0]["children"][0]["value"]
            }, {
                "attr": "重症",
                "value": data["main_summary"]["children"][0]["children"][0]["children"][1]["value"]
            }]
        }, {
            "attr": "退院",
            "value": int(mojimoji.zen_to_han(summary_text.group(3)))
        }, {
            "attr": "死亡",
            "value": int(mojimoji.zen_to_han(summary_text.group(4)))
        }]
    }]
}

# 陽性患者の属性
df_patients = df_kanjya.loc[:, ["No", "判明日", "居住地", "年代", "性別"]].fillna("-")
data["patients"] = {"date": dt_now, "data": df_patients.to_dict(orient="records")}

# 陽性患者数(居住地別)
data["patients_by_residence"] = {
    "date": dt_now,
    "data": [
        {"居住地": "A", "小計": int((df_patients["居住地"] == "富山市").sum())},
        {"居住地": "B", "小計": int((df_patients["居住地"] == "高岡市").sum())},
        {"居住地": "C", "小計": int((df_patients["居住地"] == "射水市").sum())},
        {"居住地": "D", "小計": int((df_patients["居住地"] == "南砺市").sum())},
        {"居住地": "E", "小計": int((df_patients["居住地"] == "砺波市").sum())},
        {"居住地": "F", "小計": int((df_patients["居住地"] == "氷見市").sum())},
        {"居住地": "G", "小計": int((df_patients["居住地"] == "魚津市").sum())},
        {"居住地": "H", "小計": int((df_patients["居住地"] == "黒部市").sum())},
        {"居住地": "I", "小計": int((df_patients["居住地"] == "滑川市").sum())},
        {"居住地": "J", "小計": int((df_patients["居住地"] == "小矢部市").sum())},
        {"居住地": "K", "小計": int((df_patients["居住地"] == "立山町").sum())},
        {"居住地": "L", "小計": int((df_patients["居住地"] == "入善町").sum())},
        {"居住地": "M", "小計": int((df_patients["居住地"] == "上市町").sum())},
        {"居住地": "N", "小計": int((df_patients["居住地"] == "朝日町").sum())},
        {"居住地": "O", "小計": int((df_patients["居住地"] == "舟橋村").sum())},
        {"居住地": "P", "小計": int(len(df_kanjya))-(int((df_patients["居住地"] == "富山市").sum())+int((df_patients["居住地"] == "高岡市").sum())+int((df_patients["居住地"] == "射水市").sum())+int((df_patients["居住地"] == "南砺市").sum())+int((df_patients["居住地"] == "砺波市").sum())+int((df_patients["居住地"] == "氷見市").sum())+int((df_patients["居住地"] == "魚津市").sum())+int((df_patients["居住地"] == "黒部市").sum())+int((df_patients["居住地"] == "滑川市").sum())+int((df_patients["居住地"] == "小矢部市").sum())+int((df_patients["居住地"] == "立山町").sum())+int((df_patients["居住地"] == "入善町").sum())+int((df_patients["居住地"] == "上市町").sum())+int((df_patients["居住地"] == "朝日町").sum())+int((df_patients["居住地"] == "舟橋村").sum()))},
]
}

# 陽性患者数(年代別)
data["patients_by_age"] = {
    "date": dt_now,
    "data": [
        {"年代": "0~", "小計": int((df_patients["年代"].str[:2] == "10").sum())-int((df_patients["年代"] == "10代").sum())},
        {"年代": "10~", "小計": int((df_patients["年代"] == "10代").sum())},
        {"年代": "20~", "小計": int((df_patients["年代"] == "20代").sum())},
        {"年代": "30~", "小計": int((df_patients["年代"] == "30代").sum())},
        {"年代": "40~", "小計": int((df_patients["年代"] == "40代").sum())},
        {"年代": "50~", "小計": int((df_patients["年代"] == "50代").sum())},
        {"年代": "60~", "小計": int((df_patients["年代"] == "60代").sum())},
        {"年代": "70~", "小計": int((df_patients["年代"] == "70代").sum())},
        {"年代": "80~", "小計": int((df_patients["年代"] == "80代").sum())},
        {"年代": "90~", "小計":  int(len(df_kanjya)) - ((int((df_patients["年代"].str[:2] == "10").sum())-int((df_patients["年代"] == "10代").sum()))+int((df_patients["年代"] == "10代").sum())+int((df_patients["年代"] == "20代").sum())+int(
             (df_patients["年代"] == "30代").sum()) + int((df_patients["年代"] == "40代").sum()) + int((df_patients["年代"] == "50代").sum()) + int((df_patients["年代"] == "60代").sum()) + int((df_patients["年代"] == "70代").sum()) + int((df_patients["年代"] == "80代").sum()))}
             ]
}

# 陽性患者数(性別)
data["patients_by_gender"] = {
    "date": dt_now,
    "data": [
        {"性別": "M", "小計": int((df_patients["性別"] == "男性").sum())},
        {"性別": "F", "小計": int((df_patients["性別"] == "女性").sum())},
        {"性別": "O", "小計": int(len(df_kanjya)) - (int((df_patients["性別"] == "男性").sum()) + int((df_patients["性別"] == "女性").sum()))
        }
    ]
}

# data.json上書き
df_result = codecs.open('../data/data.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
