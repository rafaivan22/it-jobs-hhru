import os
import json
import pandas as pd

def collect_data(json_path='data/raw/vacancies.json', csv_path='data/raw_jobs.csv'):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df.to_csv(csv_path, index=False)
    print(f"Raw jobs data saved to {csv_path}")
    return df

if __name__ == '__main__':
    collect_data()
