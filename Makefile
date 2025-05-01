install:
	pip install -r requirements.txt

data:
	python scripts/scrape_vacancies.py
	python data_processing.py

lint:
	flake8 .

test:
	pytest

run:
	streamlit run dashboard/app.py
