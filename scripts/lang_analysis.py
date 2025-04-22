import matplotlib.pyplot as plt
import streamlit as st


def analyze_languages(df):
    """
    Analyzes the most popular programming languages
    from the 'languagehaveworkedwith' column in a given DataFrame.
    """

    print("\n[INFO] 🔍 Analyzing most popular programming languages...")

    # Drop missing values in the column
    langs_series = df['languagehaveworkedwith'].dropna()

    # Split and explode
    langs_exploded = langs_series.str.split(';').explode().str.strip()

    # Count top languages
    top_langs = langs_exploded.value_counts().head(10)
    print("\n[INFO] Top 10 Programming Languages:")
    print(top_langs)

    # Plot
    plt.figure(figsize=(10,6))
    top_langs.plot(kind='barh', color='#4f46e5')  # Indigo for 🔥
    plt.title("Top 10 Programming Languages (Professional Developers)")
    plt.xlabel("Number of Mentions")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.clf()

    return top_langs
