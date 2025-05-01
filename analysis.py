import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path='data/clean_it_vacancies.csv'):
    return pd.read_csv(path)

def salary_distribution(df, output='plots/salary_distribution.png'):
    plt.figure()
    df['salary_mean'] = (df['salary_from'] + df['salary_to']) / 2
    df['salary_mean'].hist(bins=20)
    plt.title('Распределение средних зарплат')
    plt.xlabel('Зарплата')
    plt.ylabel('Количество вакансий')
    os.makedirs(os.path.dirname(output), exist_ok=True)
    plt.savefig(output)
    print(f"Saved salary distribution to {output}")

def top_cities(df, n=10):
    return df['area'].value_counts().head(n)

if __name__ == '__main__':
    df = load_data()
    salary_distribution(df)
    print('Top 10 городов по числу вакансий:')
    print(top_cities(df))
