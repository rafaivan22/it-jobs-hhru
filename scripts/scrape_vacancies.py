import os
import json
import yaml
import requests
from tqdm import tqdm

def load_config(path='config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def fetch_vacancies(config, per_page=100, max_pages=5):
    all_vacancies = []
    for spec in config['specializations']:
        for page in range(max_pages):
            params = {
                'text': spec,
                'per_page': per_page,
                'page': page
            }
            resp = requests.get(config['hh_api_url'], params=params)
            resp.raise_for_status()
            data = resp.json()
            all_vacancies.extend(data.get('items', []))
            if not data.get('pages') or page >= data['pages'] - 1:
                break
    return all_vacancies

def save_raw(data, output_dir='data/raw'):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, 'vacancies.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved raw data to {path}")

if __name__ == '__main__':
    cfg = load_config()
    vacancies = fetch_vacancies(cfg)
    save_raw(vacancies)
