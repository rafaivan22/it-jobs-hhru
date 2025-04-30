import requests
import pandas as pd
import time
from tqdm import tqdm
import os

SPECIALIZATIONS = ['Python', 'Java', 'Data Scientist', 'Frontend', 'Backend', 'DevOps', 'QA', '1C', 'C++', 'iOS', 'Android']
AREA = 113
PAGES = 10
BASE_URL = 'https://api.hh.ru/vacancies'
HEADERS = {'User-Agent': 'IT-job-analysis-bot'}

def fetch_vacancies(query, pages=5):
    vacancies = []
    for page in tqdm(range(pages), desc=f'Fetching: {query}'):
        params = {'text': query, 'area': AREA, 'page': page, 'per_page': 100}
        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        if response.status_code != 200:
            break
        data = response.json()
        for item in data['items']:
            salary = item.get('salary')
            vacancy = {
                'id': item['id'], 'name': item['name'], 'area': item['area']['name'], 'employer': item['employer']['name'] if item.get('employer') else None, 'published_at': item['published_at'], 'salary_from': salary['from'] if salary else None, 'salary_to': salary['to'] if salary else None, 'currency': salary['currency'] if salary else None, 'url': item['alternate_url'], 'specialization': query
            }
            vacancies.append(vacancy)
        time.sleep(0.2)
    return vacancies

def fetch_details(vacancy_id):
    url = f'https://api.hh.ru/vacancies/{vacancy_id}'
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return None, None
    data = response.json()
    desc = data.get('description', '')
    skills = [s['name'] for s in data.get('key_skills', [])]
    return desc, ', '.join(skills)

def run():
    all_vacancies = []
    for spec in SPECIALIZATIONS:
        all_vacancies.extend(fetch_vacancies(spec, PAGES))
    df = pd.DataFrame(all_vacancies)
    descriptions = []
    key_skills = []
    for vid in tqdm(df['id'], desc='Details'):
        d, k = fetch_details(vid)
        descriptions.append(d)
        key_skills.append(k)
        time.sleep(0.1)
    df['description'] = descriptions
    df['key_skills'] = key_skills
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/it_vacancies_full.csv', index=False)

if __name__ == '__main__':
    run()
# 📥 Обновление для истории коммита: сбор вакансий с API hh.ru
