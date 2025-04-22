import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from scripts.lang_analysis import analyze_languages
from scripts.remote_work import analyze_remote_work
from scripts.salary_analysis import analyze_salary
from scripts.ai_opinions import analyze_ai_opinions
from scripts.age_job_status import analyze_age_vs_job


df = pd.read_csv("data/cleaned/cleaned_survey_data.csv")

# Filter to only professional developers
df_pro = df[df['mainbranch'] == 'I am a developer by profession'].copy()

# CONFIG
st.set_page_config(page_title="Stack Overflow 2024 – Dev Insights", layout="wide")

# HEADER
st.title("💻 Developer Insights – Stack Overflow Survey 2024")
st.markdown("""
Welcome to an interactive analysis of over 50,000 professional developers.
Explore trends in programming languages, remote work, salaries, AI opinions, and age demographics.
""")

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned/cleaned_survey_data.csv")
    df = df[df['mainbranch'] == 'I am a developer by profession'].copy()
    return df

df = load_data()

# SIDEBAR
st.sidebar.header("Filters")
age_filter = st.sidebar.multiselect("Age Group", df['age'].dropna().unique())
country_filter = st.sidebar.multiselect("Country", df['country'].dropna().unique())

if age_filter:
    df = df[df['age'].isin(age_filter)]

if country_filter:
    df = df[df['country'].isin(country_filter)]

# LAYOUT
st.markdown("---")
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👨‍💻 Languages", "🌍 Remote Work", "💸 Salaries", "🤖 AI Opinions", "📊 Age & Job Status"
])

with tab1:
    st.subheader("Top Programming Languages")
    analyze_languages(df)

with tab2:
    st.subheader("Remote Work Preferences by Country")
    analyze_remote_work(df)

with tab3:
    st.subheader("Average Salary by Employment Type")
    analyze_salary(df)

with tab4:
    st.subheader("Do Developers Think AI is a Threat?")
    analyze_ai_opinions(df)

with tab5:
    st.subheader("Age Distribution by Employment Type")
    analyze_age_vs_job(df)