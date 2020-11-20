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
summary = soup.find("div", id="main").get_text(strip=True)

# 陽性患者数
total = int(mojimoji.zen_to_han(re.search(r"(\d+?)人", summary).group(1)))
# 入院中・入院等調整中
hospitalized = int(mojimoji.zen_to_han(
    re.search(r"入院中又は入院等調整中(.+?)人", summary).group(1)))
# 重症
severe = int(mojimoji.zen_to_han(re.search(r"重症者 (.+?)人", summary).group(1)))
# 無症状・軽症・中等症
mild = hospitalized - severe
# 宿泊療養
lodging = int(mojimoji.zen_to_han(re.search(r"宿泊療養施設入所者数(.+?)人", summary).group(1)))
# 死亡
death = int(mojimoji.zen_to_han(re.search(r"死亡(.+?)人", summary).group(1)))
# 退院
discharged = int(mojimoji.zen_to_han(re.search(r"退院等(.+?)人", summary).group(1)))

# 検査陽性者の状況
data["main_summary"] = {
    "attr": "陽性患者数",
    "date": dt_now,
    "value": total,
    "children": [
        {
            "attr": "入院中・入院等調整中",
            "value": hospitalized,
            "children": [
                {
                    "attr": "無症状・軽症・中等症",
                    "value":  mild
                },
                {
                    "attr": "重症",
                    "value":  severe
                }
            ]
        },
        {
            "attr": "宿泊療養",
            "value":  lodging
        },
        {
            "attr": "死亡",
            "value":  death
        },
        {
            "attr": "退院",
            "value": discharged
        }
    ]
}

# 一覧エクセルを取得
file_list = soup.find("div", id="file")
link = file_list.find(
    "a", text="富山県内における新型コロナウイルス感染症の発生状況一覧（Excelファイル）").get("href")
df_kanjya = pd.read_excel(link, skiprows=2)

# エクセル内データを定義書準拠形式に変換
df_kanjya.rename(columns={"県番号": "No"}, inplace=True)
df_kanjya["No"] = df_kanjya.index + 1
flg_is_serial = df_kanjya["検査結果判明日"].astype("str").str.isdigit()
fromSerial = pd.to_datetime(
    df_kanjya.loc[flg_is_serial, "検査結果判明日"].astype(float),
    unit="D",
    origin=pd.Timestamp("1899/12/30"),
)
fromString = pd.to_datetime(
    df_kanjya.loc[~flg_is_serial, "検査結果判明日"])
df_kanjya["検査結果判明日"] = pd.concat(
    [fromString, fromSerial])
df_kanjya.rename(columns={"検査結果判明日": "判明日"}, inplace=True)
df_kanjya["判明日"] = df_kanjya["判明日"].dt.strftime("%Y-%m-%d")
df_kanjya['性別'] = df_kanjya["性別"].replace("男", "男性").replace("女", "女性")
df_kanjya['年代'] = df_kanjya["年代"].replace("90以上", "90歳以上").replace(
    "90代", "90歳以上").replace("90代以上", "90歳以上")

# 陽性患者数
dt_start = datetime.datetime(2020, 3, 30)
dt_end = datetime.datetime.now()
patients_summary = []
while True:
    patients_summary.append({"日付": dt_start.strftime(
        '%Y-%m-%d'), "小計": int((df_kanjya["判明日"] == dt_start.strftime('%Y-%m-%d')).sum())})
    if(dt_start.strftime('%Y-%m-%d') == dt_end.strftime('%Y-%m-%d')):
      break
    dt_start += datetime.timedelta(days=1)

data["patients_summary"] = {
    "date": dt_now,
    "data": patients_summary
}

# 陽性患者の属性
df_patients = df_kanjya.loc[:, ["No", "判明日", "居住地", "年代", "性別"]].fillna("-")
data["patients"] = {"date": dt_now,
                    "data": df_patients.to_dict(orient="records")}

# 陽性患者数(年代別)
data["patients_by_age"] = {
    "date": dt_now,
    "labels": ["0~", "10~", "20~", "30~", "40~", "50~", "60~", "70~", "80~", "90~"],
    "datasets": [
        {
            "label": "M",
            "data": [
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "10歳未満")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "10代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "20代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "30代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "40代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "50代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "60代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "70代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "80代")).sum()),
                int(((df_patients["性別"] == "男性") & (
                    df_patients["年代"] == "90歳以上")).sum()),
            ]
        },
        {
            "label": "F",
            "data": [
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "10歳未満")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "10代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "20代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "30代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "40代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "50代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "60代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "70代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "80代")).sum()),
                int(((df_patients["性別"] == "女性") & (
                    df_patients["年代"] == "90歳以上")).sum()),
            ]
        },
        {
            "label": "O",
            "data": [
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "10歳未満")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "10代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "20代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "30代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "40代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "50代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "60代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "70代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "80代")).sum()),
                int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-") & (
                    df_patients["年代"] == "90歳以上")).sum()),
            ]
        }
    ]
}

# 陽性患者数(性別)
data["patients_by_gender"] = {
    "date": dt_now,
    "data": {
        "M": int((df_patients["性別"] == "男性").sum()),
        "F": int((df_patients["性別"] == "女性").sum()),
        "O": int(((df_patients["性別"] != "男性") & (df_patients["性別"] != "女性") & (df_patients["性別"] != "-")).sum())
    }
}

# data.json上書き
df_result = codecs.open('../data/data.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
