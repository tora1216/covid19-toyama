import datetime
import pandas as pd
import json

data = {}

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
data["date"] = dt_now

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJuQThafLPC7OPqUC9TbLV1DmSU0x2Co8VZi2Q2ZZCKLJCTayDl6IoXKyK676mzBgpkoKMgpNK1VML/pub?gid=574469870&single=true&output=csv"
df = pd.read_csv(URL)

# 指定した列に欠損値がある行をすべて削除
df = df.dropna(subset=['年月日'])

df_test = df.loc[:, ("年月日", "県_PCR検査数", "医療機関_PCR検査数", "医療機関_抗原検査数")].copy()
df_test.rename(
    columns={"年月日": "labels", "県_PCR検査数": "PCR検査数(県実施分)", "医療機関_PCR検査数": "PCR検査数(医療機関実施分)", "医療機関_抗原検査数": "抗原検査数(医療機関実施分)"}, inplace=True)
# 欠損値を0埋め
df_test = df_test.fillna(0)
df_test = df_test.to_dict(orient="list")
data["data"]= df_test


# test.json上書き
df_result = open('../data/test.json', 'w', encoding="utf-8")
json.dump(data, df_result, ensure_ascii=False, indent=4)
