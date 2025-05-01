import json
import pandas as pd

def clean_salary(salary_dict):
    if not salary_dict:
        return None, None
    return salary_dict.get('from'), salary_dict.get('to')

def load_raw(path='data/raw/vacancies.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_data(raw, output_csv='data/clean_it_vacancies.csv'):
    records = []
    for item in raw:
        sal_from, sal_to = clean_salary(item.get('salary'))
        record = {
            'id': item.get('id'),
            'name': item.get('name'),
            'area': item.get('area', {}).get('name'),
            'published_at': item.get('published_at'),
            'salary_from': sal_from,
            'salary_to': sal_to,
            'employer': item.get('employer', {}).get('name'),
            'url': item.get('alternate_url')
        }
        records.append(record)
    df = pd.DataFrame(records)
    df.dropna(subset=['salary_from', 'salary_to'], inplace=True)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}")
    return df

if __name__ == '__main__':
    raw = load_raw()
    clean_data(raw)
