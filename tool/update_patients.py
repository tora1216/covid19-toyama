import pandas as pd
import datetime
import json

df = pd.read_csv('../data/patients.csv', encoding='utf_8_sig')
patients = df.to_dict(orient='record')

data = {
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "data": patients
}

with open('../data/patients.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)