import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

st.set_page_config(layout='wide')

df = pd.read_csv('../data/clean_it_vacancies.csv')
df = df.dropna(subset=['salary_avg'])

st.title('📊 Исследование рынка труда в IT (по данным hh.ru)')
specializations = sorted(df['specialization'].unique())
selected_spec = st.selectbox('Выберите IT-направление', specializations)
df_filtered = df[df['specialization'] == selected_spec]
avg_salary = df_filtered['salary_avg'].mean()
st.metric('💰 Средняя зарплата', f'{avg_salary:,.0f} ₽')

city_salary = df_filtered.groupby('area')['salary_avg'].mean().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(10, 4))
city_salary.plot(kind='bar', ax=ax1, color='teal')
ax1.set_title('Средняя зарплата по городам')
ax1.set_ylabel('₽')
ax1.set_xticklabels(city_salary.index, rotation=45)
st.pyplot(fig1)

skills = []
for s in df_filtered.dropna(subset=['key_skills'])['key_skills']:
    skills += [x.strip() for x in s.split(',') if x.strip()]
skill_counts = Counter(skills).most_common(20)
skills_df = pd.DataFrame(skill_counts, columns=['Навык', 'Частота'])
fig2, ax2 = plt.subplots(figsize=(10, 4))
skills_df.plot(kind='bar', x='Навык', y='Частота', ax=ax2, legend=False, color='purple')
ax2.set_title('Топ-20 навыков')
ax2.set_xticklabels(skills_df['Навык'], rotation=45)
st.pyplot(fig2)

st.subheader('☁️ Облако навыков')
skill_text = ' '.join(skills)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(skill_text)
fig3, ax3 = plt.subplots(figsize=(12, 5))
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)