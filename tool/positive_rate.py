import pandas
from decimal import Decimal, ROUND_HALF_UP
import datetime
import json

# データURL
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSJuQThafLPC7OPqUC9TbLV1DmSU0x2Co8VZi2Q2ZZCKLJCTayDl6IoXKyK676mzBgpkoKMgpNK1VML/pub?gid=574469870&single=true&output=csv'

# データ読み込み
df = pandas.read_csv(url)

# 指定した列のいずれかに欠損値がある行をすべて削除
df = df.dropna(subset = ['年月日', '陽性人数', '陰性人数'])

# 使用する列のみ抽出して辞書型に変換
df = df.loc[:, ('年月日', '陽性人数', '陰性人数')]
df.rename(columns = {'年月日': 'diagnosed_date', '陽性人数': 'positive_count', '陰性人数': 'negative_count'}, inplace=True)
df = df.astype({'diagnosed_date': str, 'positive_count': int, 'negative_count': int})
df = df.to_dict(orient = 'recodes')

# 陽性率を算出
for data in df:
    try:
        rate = (data['positive_count'] / (data['positive_count'] + data['negative_count'])) * 100
        # 小数第二位で四捨五入
        rate = float(Decimal(str(rate)).quantize(Decimal('0.1'), ROUND_HALF_UP))
    except ZeroDivisionError:
        # ゼロ除算時の対応
        rate = 0.0
    data['positive_rate'] = rate


# 現在時刻
dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

# 整形
result_json = {'date': dt_now, 'data': df}

# 上書き保存
with open('../data/positive_rate.json', 'w') as f:
    json.dump(result_json, f, ensure_ascii = False, indent = 4)



