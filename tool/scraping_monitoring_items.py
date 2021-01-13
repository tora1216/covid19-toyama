import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import mojimoji
import json

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# 富山県HPから最新の情報を取得
url = "http://www.pref.toyama.jp/cms_sec/1205/kj00022038.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
}
r = requests.get(url, headers=headers)
r.raise_for_status()
soup = BeautifulSoup(r.content, "html.parser")

# 一覧エクセルを取得
file_list = soup.find("div", id="file")
link = file_list.find(
    "a", text="強化・緩和の判断指標（直近１週間平均）の推移").get("href")
df = pd.read_excel(link, header=None, index_col=None, engine="openpyxl")

# データ部分のみ取り出し
df = df.iloc[2:10, 3:].fillna("-")

# 反転
df = df.T

# リネーム
df.rename(columns={2: "日付", 3: "入院者数", 4: "重症病床稼働率", 5: "新規陽性者数", 6: "感染経路不明者数", 7: "陽性率"}, inplace=True)

# 日付処理
df["日付"] = df["日付"].apply(lambda x: re.search(r'\d{1,2}\/\d{1,2}', x)[0])
df.loc[:236, ["日付"]] = '2020/' + df.loc[:236, ["日付"]]
df.loc[237:, ["日付"]] = '2021/' + df.loc[237:, ["日付"]]
df["日付"] = pd.to_datetime(df["日付"], format="%Y/%m/%d")
df["日付"] = df["日付"].dt.strftime("%Y-%m-%d")

# モニタリング項目(1) 入院者数
df_hospitalized = df.loc[:, ["日付", "入院者数"]]
df_hospitalized["入院者数"] = df_hospitalized["入院者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
df_hospitalized.rename(columns={"入院者数": "小計"}, inplace=True)
data = {"date": dt_now, "data": df_hospitalized.to_dict(orient="records")}
with open('../data/monitoring/hospitalized.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# モニタリング項目(2) 重症病床稼働率
df_bed_occupancy_rate = df.loc[:, ["日付", "重症病床稼働率"]]
df_bed_occupancy_rate["重症病床稼働率"] = df_bed_occupancy_rate["重症病床稼働率"].apply(lambda x: round(x * 100, 2))
df_bed_occupancy_rate.rename(columns={"重症病床稼働率": "小計"}, inplace=True)
data = {"date": dt_now, "data": df_bed_occupancy_rate.to_dict(orient="records")}
with open('../data/monitoring/bed_occupancy_rate.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# モニタリング項目(3) 新規陽性者数
df_positives = df.loc[:, ["日付", "新規陽性者数"]]
df_positives["新規陽性者数"] = df_positives["新規陽性者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
df_positives.rename(columns={"新規陽性者数": "小計"}, inplace=True)
data = {"date": dt_now, "data": df_positives.to_dict(orient="records")}
with open('../data/monitoring/positives.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# モニタリング項目(4) 感染経路不明者数
df_untracked_infected = df.loc[:, ["日付", "感染経路不明者数"]]
df_untracked_infected["感染経路不明者数"] = df_untracked_infected["感染経路不明者数"].apply(lambda x: float(mojimoji.zen_to_han(x[:-1])))
df_untracked_infected.rename(columns={"感染経路不明者数": "小計"}, inplace=True)
data = {"date": dt_now, "data": df_untracked_infected.to_dict(orient="records")}
with open('../data/monitoring/untracked_infected.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# モニタリング項目(5) 陽性率
df_positive_rate = df.loc[:, ["日付", "陽性率"]]
df_positive_rate["陽性率"] = df_positive_rate["陽性率"].apply(lambda x: round(x * 100, 1))
df_positive_rate.rename(columns={"陽性率": "小計"}, inplace=True)
data = {"date": dt_now, "data": df_positive_rate.to_dict(orient="records")}
with open('../data/monitoring/positive_rate.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)