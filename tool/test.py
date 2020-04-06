# coding:utf-8

from datetime import datetime
import pandas as pd
import codecs
import json

COUNTS_FILE = "toyama_counts.csv"
PATIENTS_FILE = "toyama_patients.csv"

# 現在時刻
dt_now = datetime.now().strftime('%Y-%m-%d %H:%M')
data = {"lastUpdate": dt_now}

# 陽性患者の属性データ読み込み
df_kanjya = pd.read_csv(PATIENTS_FILE, index_col="No", dtype={"年代": "object"})

# 陽性患者の属性
df_kanjya.rename(columns={"公表年月日": "公表日"}, inplace=True)
df_patients = df_kanjya.loc[:, ("公表日", "居住地", "年代", "性別", "職業")]
data["patients"] = {"date": dt_now,
                    "data": df_patients.to_dict(orient="recodes")}

# 集計データ読み込み
df_counts = pd.read_csv(COUNTS_FILE)

# 陽性患者数
df_pats = df_counts.loc[:, ("年月日", "陽性人数")].copy()
df_pats.rename(columns={"年月日": "公表日", "陽性人数": "小計"}, inplace=True)
data["patients_summary"] = {"date": dt_now, "data": df_pats.to_dict(orient="recodes")}

# 検査実施人数
df_insp = df_counts.loc[:, ("年月日", "検査実施人数")].copy()
df_insp.rename(columns={"年月日": "日付", "検査実施人数": "小計"}, inplace=True)
data["inspection_persons"] = {"date": dt_now,
                              "data": df_insp.to_dict(orient="recodes")}

# 一般相談件数
df_contacts = df_counts.loc[:, ("年月日", "一般相談件数")].copy()
df_contacts.rename(columns={"年月日": "日付", "一般相談件数": "小計"}, inplace=True)
data["contacts"] = {"date": dt_now, "data": df_contacts.to_dict(orient="recodes")}

# 帰国者・接触者相談件数
df_querents = df_counts.loc[:, ("年月日", "帰国者相談件数")].copy()
df_querents.rename(columns={"年月日": "日付", "帰国者相談件数": "小計"}, inplace=True)
data["querents"] = {"date": dt_now, "data": df_querents.to_dict(orient="recodes")}

# data.json作成
df_result = codecs.open('data.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
