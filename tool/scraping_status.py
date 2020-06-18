import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import mojimoji
import json

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
df_status = pd.read_excel(link, header=None , index_col=None)
df_status = df_status.iloc[2:9, 3:]
df_status = df_status.T
df_status = df_status.sort_index(ascending=False)
df_status = df_status.to_dict(orient="records")

result = []
for status in df_status:
    data = {}
    data["日付"] = re.search(r'\d{1,2}\/\d{1,2}', status[2])[0]
    data["入院者数"] = float(mojimoji.zen_to_han(status[3][:-1]))
    data["重症病床稼働率"] = round(status[4]*100,2)
    data["新規陽性者数"] = float(mojimoji.zen_to_han(status[5][:-1]))
    data["感染経路不明者数"] = float(mojimoji.zen_to_han(status[6][:-1]))
    data["陽性率"] = round(status[7]*100,2)
    data["達成状況"] = status[8]
    result.append(data)

data = {
    "statusItems": result}

# data.json上書き
df_result = open('../data/status.json', 'w', encoding="utf-8")
json.dump(data, df_result, ensure_ascii=False, indent=4)



