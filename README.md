#  Исследование рынка труда в сфере IT на основе данных hh.ru

##  Цель проекта

Провести анализ IT-вакансий на российском рынке труда на основе данных HeadHunter:

  * Какие направления востребованы?
  * Какие зарплаты предлагают?
  * Какие навыки требуют работодатели?
  * Как распределяется спрос по городам?

Проект выполнен в рамках учебного мини-исследования.

* * *
##  Структура проекта
    ├── README.md               <- Описание проекта, авторов, инструкции
    ├── requirements.txt        <- Все зависимости для запуска проекта
    ├── config.yaml             <- Конфигурация скриптов
    ├── notebooks               <- Jupyter ноутбуки (очистка, анализ, визуализация)
    │   ├── 1_data_cleaning.ipynb
    │   ├── 2_analysis.ipynb
    │   └── 3_visualization.ipynb
    ├── scripts                 <- Python-скрипты (сбор данных)
    │   └── scrape_vacancies.py
    ├── data                    <- Все используемые и полученные данные
    │   ├── raw
    │   │   └── vacancies.json
    │   └── clean_it_vacancies.csv
    ├── dashboard               <- Streamlit-дэшборд
    │   └── app.py
    ├── tests                   <- Тесты проекта
    ├── Dockerfile
    ├── .gitignore
    ├── .flake8
    ├── Makefile
    └── .github/workflows
        └── ci.yml

* * *
##  Быстрый старт

1. Установите зависимости:
```
pip install -r requirements.txt
```
2. Соберите данные с hh.ru:
```
python scripts/scrape_vacancies.py
```
3. Очистите данные:
```
python data_processing.py
```
4. Запустите дашборд:
```
streamlit run dashboard/app.py
```
