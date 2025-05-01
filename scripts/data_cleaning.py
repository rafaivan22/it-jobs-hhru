import os
import pandas as pd

def clean_jobs_data(input_csv='data/raw_jobs.csv', output_csv='data/cleaned_jobs.csv'):
    df = pd.read_csv(input_csv)
    # Placeholder for cleaning logic; currently copies data
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Cleaned jobs data saved to {output_csv}")
    return df

if __name__ == '__main__':
    clean_jobs_data()
