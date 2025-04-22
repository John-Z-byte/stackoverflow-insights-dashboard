import matplotlib.pyplot as plt
import streamlit as st

def analyze_ai_opinions(df):
    """
    Analyzes developer sentiment and opinions on AI.
    """

    print("\n[INFO] 🤖 Analyzing developer AI opinions...")

    # Filter columns related to AI
    ai_cols = ['aithreat']
    df_ai = df[ai_cols].dropna(how='all')

    for col in ai_cols:
        print(f"\n[INFO] {col.upper()} Responses:")
        print(df_ai[col].value_counts(dropna=True, normalize=True) * 100)

        # Plot
        plt.figure(figsize=(8,4))
        df_ai[col].value_counts().plot(kind='barh', color='#6366f1')  # Indigo
        plt.title(f"Do you believe AI poses a threat to your job? {col}")
        plt.xlabel("Number of Respondents")
        plt.tight_layout()
        st.pyplot(plt)
        
        return df_ai
