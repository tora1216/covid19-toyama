# coding:utf-8

from datetime import datetime
import pandas as pd
import codecs
import json

# 陽性患者の属性データ
PATIENTS_FILE = "toyama_patients.csv"
# 集計データ
COUNTS_FILE = "toyama_counts.csv"

# 現在時刻
dt_now = datetime.now().strftime('%Y-%m-%d %H:%M')
data = {"lastUpdate": dt_now}

# 集計データ読み込み
df_counts = pd.read_csv(COUNTS_FILE)

# 陽性患者の属性データ読み込み
df_kanjya = pd.read_csv(PATIENTS_FILE)

# 検査実施状況
data["inspection_status_summary"] = {"date": dt_now, "children": [{"attr": "陽性人数", "value": int(len(df_kanjya))},{"attr": "陰性人数", "value": int(df_counts["陰性人数"].sum())}]}

# 陽性患者の属性
df_kanjya.rename(columns={"公表年月日": "公表日"}, inplace=True)
df_patients = df_kanjya.loc[:, ("公表日", "居住地", "年代", "性別")].fillna("-")
data["patients"] = {"date": dt_now, "data": df_patients.to_dict(orient="recodes")}

# 居住地別陽性患者数
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
        {"居住地": "O", "小計": int((df_patients["居住地"] == "船橋村").sum())},
        {"居住地": "P", "小計":  int(len(df_kanjya))-(int((df_patients["居住地"] == "富山市").sum())+int((df_patients["居住地"] == "高岡市").sum())+int((df_patients["居住地"] == "射水市").sum())+int((df_patients["居住地"] == "南砺市").sum())+int((df_patients["居住地"] == "砺波市").sum())+int((df_patients["居住地"] == "氷見市").sum())+int((df_patients["居住地"] == "魚津市").sum())+int((df_patients["居住地"] == "黒部市").sum())+int((df_patients["居住地"] == "滑川市").sum())+int((df_patients["居住地"] == "小矢部市").sum())+int((df_patients["居住地"] == "立山町").sum())+int((df_patients["居住地"] == "入善町").sum())+int((df_patients["居住地"] == "上市町").sum())+int((df_patients["居住地"] == "朝日町").sum())+int((df_patients["居住地"] == "船橋村").sum()))},
]
}

# 年齢別陽性患者数
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
             (df_patients["年代"] == "30代").sum())+int((df_patients["年代"] == "40代").sum())+int((df_patients["年代"] == "50代").sum())+int((df_patients["年代"] == "60代").sum())+int((df_patients["年代"] == "70代").sum())+int((df_patients["年代"] == "80代").sum()))},
]
}

# 陽性患者数
df_pats = df_counts.loc[:, ("年月日", "陽性人数")].copy()
df_pats.rename(columns={"年月日": "日付", "陽性人数": "小計"}, inplace=True)
data["patients_summary"] = {"date": dt_now, "data": df_pats.to_dict(orient="recodes")}

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

# data.json作成
df_result = codecs.open('../data/data.json', 'w', 'utf-8')
json.dump(data, df_result, ensure_ascii=False, indent=4)
