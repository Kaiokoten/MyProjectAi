# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="수면과 건강 분석",
    layout="wide",
    page_icon="🛏️"
)

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
    return df

df = load_data()

# 제목
st.title("🛏️ 수면과 건강 분석 대시보드")
st.markdown("이 웹사이트는 수면 시간과 건강 지표(스트레스, 심박수, 수면 질 등) 간의 관계를 시각화합니다.")

# 인터랙티브 필터
st.sidebar.header("🔎 필터 옵션")
gender_filter = st.sidebar.multiselect("성별 선택", options=df["Gender"].unique(), default=df["Gender"].unique())
occupation_filter = st.sidebar.multiselect("직업 선택", options=df["Occupation"].unique(), default=df["Occupation"].unique())
age_range = st.sidebar.slider("나이 범위", int(df["Age"].min()), int(df["Age"].max()), (20, 60))

# 필터 적용
filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Occupation"].isin(occupation_filter)) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

# 주요 지표
st.subheader("📊 주요 통계")
col1, col2, col3 = st.columns(3)
col1.metric("평균 수면 시간", f"{filtered_df['Sleep Duration'].mean():.2f} 시간")
col2.metric("평균 스트레스 수준", f"{filtered_df['Stress Level'].mean():.1f}/10")
col3.metric("평균 심박수", f"{filtered_df['Heart Rate'].mean():.0f} bpm")

# 수면 시간 분포
st.subheader("🛌 수면 시간 분포")
fig1 = px.histogram(filtered_df, x="Sleep Duration", nbins=20, title="수면 시간 분포", color="Gender")
st.plotly_chart(fig1, use_container_width=True)

# 수면 시간과 스트레스
st.subheader("🧠 수면 시간과 스트레스 관계")
fig2 = px.scatter(filtered_df, x="Sleep Duration", y="Stress Level", color="Gender",
                  title="수면 부족 = 스트레스 증가?")
st.plotly_chart(fig2, use_container_width=True)

# 수면 시간과 심박수
st.subheader("❤️ 수면 시간과 심박수 관계")
fig3 = px.scatter(filtered_df, x="Sleep Duration", y="Heart Rate", color="Gender",
                  title="수면과 심박수는 어떤 관련이 있을까?")
st.plotly_chart(fig3, use_container_width=True)

# BMI와 수면 질
st.subheader("📉 체질량 지수(BMI)와 수면 질")
fig4 = px.box(filtered_df, x="BMI Category", y="Quality of Sleep", color="BMI Category",
              title="체형과 수면 질의 관계")
st.plotly_chart(fig4, use_container_width=True)

# 수면 장애 분석
st.subheader("😵 수면 장애와 수면 시간")
fig5 = px.box(filtered_df, x="Sleep Disorder", y="Sleep Duration", color="Sleep Disorder",
              title="수면 장애가 수면 시간에 미치는 영향")
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.markdown("👨‍💻 제작자: 정 예고르/ Ten Egor | 데이터 출처: Sleep Health & Lifestyle Dataset")


