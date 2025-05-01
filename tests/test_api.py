import pytest
from scripts.scrape_vacancies import fetch_vacancies, load_config

def test_load_config():
    cfg = load_config()
    assert 'hh_api_url' in cfg
