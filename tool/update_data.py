# coding:utf-8

import json
import codecs
import datetime
import pandas as pd

# 現時点のデータを取得
data = json.load(codecs.open('../data/data.json', 'r', 'utf-8'))

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
data["lastUpdate"] = dt_now

# 集計データ
COUNTS_FILE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJuQThafLPC7OPqUC9TbLV1DmSU0x2Co8VZi2Q2ZZCKLJCTayDl6IoXKyK676mzBgpkoKMgpNK1VML/pub?gid=574469870&single=true&output=csv"

# 集計データ読み込み
df_counts = pd.read_csv(COUNTS_FILE)

# 指定した列のいずれかに欠損値がある行をすべて削除
df_counts = df_counts.dropna(subset=['年月日', '陰性人数', '陽性人数', '一般相談件数', '帰国者相談件数', '退院者数', '死亡者数'])

# 欠損値を0埋め
df_counts = df_counts.fillna(0)

# データ形式の指定
df_counts = df_counts.astype({'年月日': str, '県_PCR検査数': int, '医療機関_PCR検査数': int, '医療機関_抗原検査数': int, '陰性人数': int, '陽性人数': int, '一般相談件数': int, '帰国者相談件数': int, '退院者数': int, '死亡者数': int})

# 死亡者数
df_dead = df_counts.loc[:, ("年月日", "死亡者数")].copy()
df_dead.rename(columns={"年月日": "日付", "死亡者数": "小計"}, inplace=True)
data["dead_persons"] = {"date": dt_now, "data": df_dead.to_dict(orient="recodes")}

# 退院者数
df_disc = df_counts.loc[:, ("年月日", "退院者数")].copy()
df_disc.rename(columns={"年月日": "日付", "退院者数": "小計"}, inplace=True)
data["discharged_persons"] = {"date": dt_now, "data": df_disc.to_dict(orient="recodes")}

# 検査実施状況
data["inspection_status_summary"] = {"date": dt_now, "children": [{"attr": "陽性人数", "value": int(df_counts["陽性人数"].sum())}, {"attr": "陰性人数", "value": int(df_counts["陰性人数"].sum())}]}

# 検査実施人数
df_insp = df_counts.loc[:, ("年月日", "県_PCR検査数")].copy()
df_insp.rename(columns={"年月日": "日付", "県_PCR検査数": "小計"}, inplace=True)
data["inspection_persons"] = {"date": dt_now, "data": df_insp.to_dict(orient="recodes")}

# 陽性率
df_rate = df_counts.loc[:, ["年月日", "県_PCR検査数", "医療機関_PCR検査数", "陽性人数"]].set_index("年月日").copy()
df_positive_7d = df_rate.rolling(window=7).mean()
df_positive_7d["陽性率"] = df_positive_7d["陽性人数"] / (df_positive_7d["県_PCR検査数"] + df_positive_7d["医療機関_PCR検査数"]) * 100
positive_rate_data = df_positive_7d["陽性率"].fillna(0).round(2).reset_index()
positive_rate_data.rename(columns={"年月日": "日付", "陽性率": "小計"}, inplace=True)
data["positive_rate"] = {"date": dt_now, "data": positive_rate_data.to_dict(orient="recodes")}

# 一般相談件数
df_contacts = df_counts.loc[:, ("年月日", "一般相談件数")].copy()
df_contacts.rename(columns={"年月日": "日付", "一般相談件数": "小計"}, inplace=True)
data["contacts"] = {"date": dt_now, "data": df_contacts.to_dict(orient="recodes")}

# 帰国者・接触者相談件数
df_querents = df_counts.loc[:, ("年月日", "帰国者相談件数")].copy()
df_querents.rename(columns={"年月日": "日付", "帰国者相談件数": "小計"}, inplace=True)
data["querents"] = {"date": dt_now, "data": df_querents.to_dict(orient="recodes")}

# data.json上書き
df_result = codecs.open('../data/data.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
