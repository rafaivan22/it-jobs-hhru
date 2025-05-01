import pandas as pd
from data_processing import clean_data

def test_clean_data(tmp_path):
    raw = [{'id':'1','name':'Test','area':{'name':'Moscow'},'published_at':'2025-01-01T00:00:00','salary':{'from':100,'to':200},'employer':{'name':'X'},'alternate_url':'url'}]
    df = clean_data(raw, output_csv=str(tmp_path/'out.csv'))
    assert isinstance(df, pd.DataFrame)
    assert 'salary_from' in df.columns
