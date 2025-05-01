import streamlit as st
import pandas as pd
import plotly.express as px

st.title('IT-рынок труда на HH.ru')

@st.cache_data
def load_data():
    df = pd.read_csv('data/clean_it_vacancies.csv')
    df['salary_mean'] = (df['salary_from'] + df['salary_to']) / 2
    return df

df = load_data()

cities = df['area'].unique()
city = st.sidebar.selectbox('Город', sorted(cities))
filtered = df[df['area'] == city]

st.header(f'Вакансии в {city}')
fig = px.histogram(filtered, x='salary_mean', nbins=20, title='Распределение средних зарплат')
st.plotly_chart(fig, use_container_width=True)
