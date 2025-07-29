import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 Brand Price Change Dashboard")

# Load data
df = pd.read_csv("Thunderbit_Cleaned.csv")

# Sidebar filter
brand = st.sidebar.selectbox("Choose a brand", df['Brand'].unique())

# Brand specific info
st.subheader(f"Details for {brand}")
st.write(df[df['Brand'] == brand])

# Percent Change Distribution
st.subheader("Distribution of Percent Change")
fig, ax = plt.subplots()
sns.histplot(df['Percent_Change'], kde=True, ax=ax)
st.pyplot(fig)

# Cluster view (if added)
if 'Cluster' in df.columns:
    st.subheader("Boxplot of % Change by Cluster")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x='Cluster', y='Percent_Change', ax=ax2)
    st.pyplot(fig2)
