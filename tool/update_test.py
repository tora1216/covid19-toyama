import datetime
import pandas as pd
import json

data = {}

# 現在時刻
dt_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

data["date"] = dt_now

# 最新データ取得
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSJuQThafLPC7OPqUC9TbLV1DmSU0x2Co8VZi2Q2ZZCKLJCTayDl6IoXKyK676mzBgpkoKMgpNK1VML/pub?gid=574469870&single=true&output=csv"
df = pd.read_csv(URL)

# 指定した列のいずれかに欠損値がある行をすべて削除
df = df.dropna(subset=['年月日', '陰性人数', '陽性人数', '一般相談件数', '受診・相談センター相談件数', '退院者数', '死亡者数'])

# 必要なデータを取り出し
df_test = df.loc[:, ("年月日", "PCR検査数", "抗原検査数")].copy()

# 欠損値を0埋め
df_test = df_test.fillna(0)

# データ形式指定
df_test['年月日'] = pd.to_datetime(df_test['年月日'])
df_test['年月日'] = df_test['年月日'].dt.strftime('%Y/%m/%d')
df_test = df_test.astype({'年月日': str, 'PCR検査数': int, '抗原検査数': int})

# 辞書型に変換
df_test = df_test.to_dict(orient="list")

data["data"]= df_test

# test.json上書き
df_result = open('../data/test.json', 'w', encoding="utf-8")
json.dump(data, df_result, ensure_ascii=False, indent=4)
