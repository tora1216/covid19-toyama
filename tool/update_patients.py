import pandas as pd

df = pd.read_csv('../data/patients.csv', encoding='utf_8_sig')
with open('../data/patients.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False, orient='records')