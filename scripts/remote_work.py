import matplotlib.pyplot as plt
import streamlit as st

def analyze_remote_work(df):
    """
    Analyzes remote work preferences by country.
    """

    print("\n[INFO]  Analyzing remote work distribution by country...")

    # Drop missing data
    df_filtered = df[['country', 'remotework']].dropna()

    # Count total responses per country
    country_counts = df_filtered['country'].value_counts()

    # Filter to countries with at least 100 responses
    valid_countries = country_counts[country_counts >= 100].index

    # Then calculate percentages only for valid countries
    remote_dist = (
        df_filtered[df_filtered['country'].isin(valid_countries)]
        .groupby('country')['remotework']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .sort_values(by='Remote', ascending=False)
    )

    # Limit to top 10 countries by % of remote devs
    top_remote = remote_dist.head(10)

    print("\n[INFO] Top 10 Countries by % of Remote Developers:")
    print(top_remote['Remote'])

    # Plot
    plt.figure(figsize=(10,6))
    top_remote['Remote'].plot(kind='barh', color='#10b981')  # emerald green
    plt.title("Top 10 Countries by % of Remote Developers")
    plt.xlabel("Proportion of Remote Devs")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    st.pyplot(plt.gcf())  
    plt.clf()  

    return top_remote
