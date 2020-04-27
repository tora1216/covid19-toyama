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

# 陽性患者の属性データ
PATIENTS_FILE = "toyama_patients.csv"
# 集計データ
COUNTS_FILE = "toyama_counts.csv"

# 陽性患者の属性データ読み込み
df_kanjya = pd.read_csv(PATIENTS_FILE)
# 集計データ読み込み
df_counts = pd.read_csv(COUNTS_FILE)

# 検査陽性者の状況
data["main_summary"] = {
    "date": dt_now,
    "children": [{
        "attr": "陽性患者数",
        "value": data["main_summary"]["children"][0]["value"],
        "children": [{
            "attr": "入院",
            "value": data["main_summary"]["children"][0]["children"][0]["value"],
            "children": [{
                "attr": "無症状・軽症・中等症",
                "value": int(((df_kanjya["状態"] == "入院中") & (df_kanjya["症状"] == "無症状")).sum())+int(((df_kanjya["状態"] == "入院中") & (df_kanjya["症状"] == "軽症・中等症")).sum())
            },{
                "attr": "重症",
                "value": int(((df_kanjya["状態"] == "入院中") & (df_kanjya["症状"] == "重症")).sum())
            }]
        },{
            "attr": "退院",
            "value": data["main_summary"]["children"][0]["children"][1]["value"]
        },{
        "attr": "死亡",
            "value": data["main_summary"]["children"][0]["children"][2]["value"]
        }]
    }]
}

# 検査実施状況
data["inspection_status_summary"] = {"date": dt_now, "children": [{"attr": "陽性人数", "value": int(df_counts["陽性人数"].sum())}, {"attr": "陰性人数", "value": int(df_counts["陰性人数"].sum())}]}

# 検査実施人数
df_insp = df_counts.loc[:, ("年月日", "検査実施人数")].copy()
df_insp.rename(columns={"年月日": "日付", "検査実施人数": "小計"}, inplace=True)
data["inspection_persons"] = {"date": dt_now, "data": df_insp.to_dict(orient="recodes")}

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
