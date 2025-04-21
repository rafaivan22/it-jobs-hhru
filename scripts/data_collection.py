import requests
import time
import csv
from pathlib import Path

KEYWORDS = ["Python", "Frontend", "Java", "Data Analyst"]
REGION = 113
PER_PAGE = 50
PAGES = 2
OUTPUT_FILE = Path("data/raw_jobs.csv")
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def get_vacancies(keyword):
    print(f"Сбор данных по ключу: {keyword}")
    all_vacancies = []
    for page in range(PAGES):
        url = "https://api.hh.ru/vacancies"
        params = {"text": keyword, "area": REGION, "per_page": PER_PAGE, "page": page}
        response = requests.get(url, params=params)
        if response.status_code != 200: continue
        data = response.json()
        for item in data["items"]:
            vacancy = {
                "id": item.get("id"),
                "name": item.get("name"),
                "area": item.get("area", {}).get("name"),
                "employer": item.get("employer", {}).get("name"),
                "salary_from": item.get("salary", {}).get("from"),
                "salary_to": item.get("salary", {}).get("to"),
                "currency": item.get("salary", {}).get("currency"),
                "published_at": item.get("published_at"),
                "keyword": keyword
            }
            detail = requests.get(f"https://api.hh.ru/vacancies/{vacancy['id']}")
            if detail.status_code == 200:
                skills = [s["name"] for s in detail.json().get("key_skills", [])]
                vacancy["key_skills"] = ", ".join(skills)
            else:
                vacancy["key_skills"] = ""
            all_vacancies.append(vacancy)
        time.sleep(1)
    return all_vacancies

def save_to_csv(vacancies, filename):
    if not vacancies: return
    with open(filename, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=vacancies[0].keys())
        writer.writeheader()
        writer.writerows(vacancies)

def main():
    all_data = []
    for kw in KEYWORDS:
        all_data.extend(get_vacancies(kw))
    save_to_csv(all_data, OUTPUT_FILE)

if __name__ == "__main__":
    main()