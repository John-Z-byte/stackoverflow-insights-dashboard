import matplotlib.pyplot as plt
import streamlit as st

def analyze_salary(df):
    """
    Analyzes average salary by employment type and professional experience.
    """

    print("\n[INFO]  Analyzing salary distribution...")

    # Step 1: Drop missing or invalid salary data
    df = df[['employment', 'yearscodepro', 'comptotal']].dropna()

    # Step 2: Clean the salary column (remove commas, $, convert to float)
    df['comptotal'] = (
        df['comptotal']
        .astype(str)
        .str.replace('[^0-9.]', '', regex=True)
        .astype(float)
    )

    # Step 3: Remove unrealistic values (like > $1 million or < $1k)
    df = df[(df['comptotal'] > 1000) & (df['comptotal'] < 1_000_000)]

    # Step 4: Normalize text to avoid duplicates
    # Step 4: Normalize and simplify employment types
    df['employment'] = (
        df['employment']
        .astype(str)
        .str.split(';')              # Split multi-labels
        .str[0]                      # Take the first one
        .str.strip()
        .str.lower()
    )

    # Average salary by cleaned employment type
    emp_salary = df.groupby('employment')['comptotal'].mean().sort_values(ascending=False)



    # Step 5: Plot
    plt.figure(figsize=(10,6))
    emp_salary.plot(kind='barh', color='#f59e0b')  # amber yellow
    plt.title("Average Salary by Employment Type")
    plt.xlabel("Average Salary (USD)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    st.pyplot(plt.gcf())  # Renders in Streamlit
    plt.clf()

    return emp_salary
