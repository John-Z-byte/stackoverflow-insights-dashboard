import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def analyze_age_vs_job(df):
    """
    Shows employment distribution by age group using a stacked bar chart.
    """

    print("\n[INFO]  Analyzing age distribution by job status...")

    # Drop rows with missing values
    df_filtered = df[['age', 'employment']].dropna()

    # Normalize employment labels
    df_filtered['employment'] = df_filtered['employment'].str.strip().str.lower()
    df_filtered['employment'] = df_filtered['employment'].replace({
        'i am employed full-time': 'full-time',
        'i am employed part-time': 'part-time',
        'i freelance': 'freelance',
        'i am a student': 'student',
        'i am currently unemployed': 'unemployed',
        'i am a contractor': 'contractor',
        'i am retired': 'retired',
        'looking for work': 'unemployed',
        'not employed, but looking for work': 'unemployed',
        'not employed and not looking for work': 'unemployed',
        'student, full-time': 'student',
        'student, part-time': 'student',
        'independent contractor, freelancer, or self-employed': 'freelance',
    })

    # Limit to top employment types
    valid_employment = ['full-time', 'part-time', 'freelance', 'student', 'unemployed']
    df_filtered = df_filtered[df_filtered['employment'].isin(valid_employment)]

    # Count values
    cross_tab = pd.crosstab(df_filtered['age'], df_filtered['employment'], normalize='index') * 100

    print("\n[INFO] Employment Distribution by Age Group (%):")
    print(cross_tab)

    # Plot
    cross_tab.plot(kind='bar', stacked=True, figsize=(10,6), colormap='tab20c')
    plt.title("Employment Type by Age Group (in %)")
    plt.ylabel("Percentage")
    plt.xlabel("Age Group")
    plt.legend(title="Employment Type", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)

    return cross_tab
