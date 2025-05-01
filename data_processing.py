import os
import json
import pandas as pd

def clean_salary(s):
    if not s:
        return None, None
    return s.get('from'), s.get('to')

def load_raw(path='data/raw/vacancies.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_data(raw, output_csv='data/clean_it_vacancies.csv'):
    records = []
    for item in raw:
        fmin, fmax = clean_salary(item.get('salary'))
        rec = {
            'id': item.get('id'),
            'name': item.get('name'),
            'area': item.get('area', {}).get('name'),
            'published_at': item.get('published_at'),
            'salary_from': fmin,
            'salary_to': fmax,
            'employer': item.get('employer', {}).get('name'),
            'url': item.get('alternate_url')
        }
        records.append(rec)
    df = pd.DataFrame(records)
    df.dropna(subset=['salary_from', 'salary_to'], inplace=True)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}")
    return df

if __name__ == '__main__':
    raw = load_raw()
    clean_data(raw)
