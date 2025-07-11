# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Настройки страницы
st.set_page_config(
    page_title="Анализ сна и здоровья",
    layout="wide",
    page_icon="😴"
)

st.title("😴 Анализ сна и здоровья")
st.markdown("Изучим, как **длительность сна** влияет на здоровье человека по различным показателям.")

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
    return df

df = load_data()

# Основная статистика
st.subheader("📊 Общая статистика")
col1, col2, col3 = st.columns(3)
col1.metric("Средняя продолжительность сна", f"{df['Sleep Duration'].mean():.2f} часов")
col2.metric("Средний уровень стресса", f"{df['Stress Level'].mean():.1f}/10")
col3.metric("Средний пульс", f"{df['Heart Rate'].mean():.0f} уд/мин")

# Распределение продолжительности сна
st.subheader("🛌 Распределение продолжительности сна")
fig1 = px.histogram(df, x="Sleep Duration", nbins=20, title="Распределение количества сна")
st.plotly_chart(fig1, use_container_width=True)

# Связь: Длительность сна и стресс
st.subheader("🧠 Связь между сном и уровнем стресса")
fig2 = px.scatter(df, x="Sleep Duration", y="Stress Level", color="Gender",
                  title="Меньше сна — больше стресса?")
st.plotly_chart(fig2, use_container_width=True)

# Связь: Длительность сна и пульс
st.subheader("❤️ Связь между сном и пульсом")
fig3 = px.scatter(df, x="Sleep Duration", y="Heart Rate", color="Gender",
                  title="Как сон влияет на частоту сердцебиения?")
st.plotly_chart(fig3, use_container_width=True)

# Качество сна по категориям
st.subheader("🌙 Качество сна по категориям ИМТ")
fig4 = px.box(df, x="BMI Category", y="Quality of Sleep", color="BMI Category",
              title="Качество сна и масса тела")
st.plotly_chart(fig4, use_container_width=True)

# Расстройства сна
st.subheader("😵 Расстройства сна и длительность сна")
fig5 = px.box(df, x="Sleep Disorder", y="Sleep Duration", color="Sleep Disorder",
              title="Связь между расстройствами сна и длительностью сна")
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.markdown("🧑‍💻 Автор: Егор | Данные: Sleep Health & Lifestyle Dataset")


