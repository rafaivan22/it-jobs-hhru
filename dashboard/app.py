import streamlit as st
import pandas as pd
import plotly.express as px

st.title('IT-рынок труда на HH.ru')
df = pd.read_csv('data/clean_it_vacancies.csv')
df['salary_mean'] = (df['salary_from'] + df['salary_to']) / 2

city = st.sidebar.selectbox('Город', df['area'].unique())
filtered = df[df['area'] == city]

st.header(f'Анализ вакансий в {city}')
fig = px.histogram(filtered, x='salary_mean', nbins=20, title='Распределение зарплат')
st.plotly_chart(fig, use_container_width=True)

skills = st.sidebar.multiselect('Навыки (пример)', ['Python', 'Java', 'SQL'], default=['Python'])
# Placeholder for skill filtering
st.write('Навыки фильтрация в разработке...')
