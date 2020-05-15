# coding:utf-8

import json
import codecs
import datetime
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP

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
df_counts = df_counts.dropna(subset=['年月日', '検査実施人数', '陰性人数', '陽性人数', '一般相談件数', '帰国者相談件数'])

# データ形式の指定
df_counts = df_counts.astype({'年月日': str, '検査実施人数': int, '陰性人数': int, '陽性人数': int, '一般相談件数': int, '帰国者相談件数': int})

# 検査実施状況
data["inspection_status_summary"] = {"date": dt_now, "children": [{"attr": "陽性人数", "value": int(df_counts["陽性人数"].sum())}, {"attr": "陰性人数", "value": int(df_counts["陰性人数"].sum())}]}

# 検査実施人数
df_insp = df_counts.loc[:, ("年月日", "検査実施人数")].copy()
df_insp.rename(columns={"年月日": "日付", "検査実施人数": "小計"}, inplace=True)
data["inspection_persons"] = {"date": dt_now, "data": df_insp.to_dict(orient="recodes")}

# 陽性率の推移
df_rate = df_counts.loc[:, ("年月日", "陽性人数", "陰性人数")].copy()
df_rate = df_rate.iloc[32:,:]
df_rate = df_rate.to_dict(orient='recodes')
positive_rate_data=[]
# 陽性率を算出
for rate_data in df_rate:
    try:
        rate = (rate_data['陽性人数'] / (rate_data['陽性人数'] + rate_data['陰性人数'])) * 100
        # 小数第二位で四捨五入
        rate = float(Decimal(str(rate)).quantize(Decimal('0.1'), ROUND_HALF_UP))
    except ZeroDivisionError:
        # ゼロ除算時の対応
        rate = 0.0
    positive_rate_data.append({"日付": rate_data["年月日"], "小計": rate})
data["positive_rate"] = {"date": dt_now, "data": positive_rate_data}

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
