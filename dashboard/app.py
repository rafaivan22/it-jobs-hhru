import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="IT Jobs in Russia", layout="wide")

df = pd.read_csv("data/cleaned_jobs.csv", parse_dates=["published_at"])
df["month"] = df["published_at"].dt.to_period("M")

st.title("💼 Анализ IT-вакансий (hh.ru)")

# Фильтры
st.sidebar.header("🔍 Фильтры")
keywords = st.sidebar.multiselect("Направления:", df["keyword"].unique(), default=list(df["keyword"].unique()))
cities = st.sidebar.multiselect("Города:", df["city"].unique(), default=list(df["city"].unique()))
salary_min, salary_max = st.sidebar.slider("Средняя зарплата (RUB):", 0, int(df["avg_salary"].max()), (0, int(df["avg_salary"].max())))

filtered_df = df[
    df["keyword"].isin(keywords) &
    df["city"].isin(cities) &
    df["avg_salary"].between(salary_min, salary_max)
]

st.markdown(f"**Вакансий после фильтрации:** {len(filtered_df)}")

col1, col2, col3 = st.columns(3)
col1.metric("💼 Вакансий", len(filtered_df))
col2.metric("💰 Средняя зарплата", f"{filtered_df['avg_salary'].mean():,.0f} RUB")
col3.metric("📍 Городов", filtered_df['city'].nunique())

# Зарплаты по направлениям
st.subheader("💸 Средняя зарплата по направлениям")
st.bar_chart(filtered_df.groupby("keyword")["avg_salary"].mean())

# Динамика по времени
st.subheader("📈 Динамика вакансий по месяцам")
trend = filtered_df.groupby("month").size()
st.line_chart(trend)

# Облако слов по навыкам
st.subheader("🔧 Популярные навыки")
skills = filtered_df["key_skills"].dropna().str.lower().str.split(", ").explode()
text = " ".join(skills)
wc = WordCloud(width=800, height=300, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10, 4))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Таблица
st.subheader("📋 Таблица вакансий")
st.dataframe(filtered_df[["vacancy_name", "city", "avg_salary", "employer_name", "key_skills", "published_at"]])