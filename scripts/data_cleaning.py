import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw_jobs.csv")
CLEAN_PATH = Path("data/cleaned_jobs.csv")

def clean_data():
    df = pd.read_csv(RAW_PATH)

    def get_avg_salary(row):
        if pd.notnull(row["salary_from"]) and pd.notnull(row["salary_to"]):
            return (row["salary_from"] + row["salary_to"]) / 2
        elif pd.notnull(row["salary_from"]):
            return row["salary_from"]
        elif pd.notnull(row["salary_to"]):
            return row["salary_to"]
        return None

    df["avg_salary"] = df.apply(get_avg_salary, axis=1)
    df["published_at"] = pd.to_datetime(df["published_at"])
    df.drop_duplicates(subset="id", inplace=True)
    df.rename(columns={"name": "vacancy_name", "area": "city", "employer": "employer_name"}, inplace=True)
    df = df[["id", "vacancy_name", "city", "employer_name", "avg_salary", "currency", "published_at", "key_skills", "keyword"]]
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Файл сохранён: {CLEAN_PATH}")

if __name__ == "__main__":
    clean_data()