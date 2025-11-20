import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

st.title("CORD-19 Data Explorer")

# Load data
df = pd.read_csv('metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_clean = df.dropna(subset=['year'])

# Show sample data
st.subheader("Sample Data")
st.dataframe(df_clean.head())

# Publications per year
st.subheader("Publications by Year")
year_counts = df_clean['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index.astype(int), y=year_counts.values, ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
titles_text = " ".join(df_clean['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
fig2, ax2 = plt.subplots(figsize=(10,5))
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis('off')
st.pyplot(fig2)
