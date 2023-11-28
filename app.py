import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from streamlit_lottie import st_lottie

def custom_css():
    st.markdown("""
        <style>
        h1 {
            color: #FF6347;
            text-align: center;
        }
        h2 {
            color: #FFA07A;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """, unsafe_allow_html=True)

st.set_page_config(page_title="My Webpage", page_icon=":tada:")

custom_css()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/5ae5c403-6777-4ddc-9d4b-69b991f2244e/SrRQPFgsnv.json")

st.title('Anime Data Visualization')

with st.container():
    st.write("---")
    st_lottie(lottie_coding, height=300, key="coding")

# Loading data
@st.cache_data 
def load_data():
    data = pd.read_csv('anime.csv') 
    data['Score'] = pd.to_numeric(data['Score'], errors='coerce')
    return data.dropna(subset=['Score', 'Type'])

data = load_data()

st.subheader('Quantitative Question')
st.write("""
What is the distribution of average scores across different types of anime (e.g., TV, Movie, OVA)?
""")

# Displaying subset of data
st.subheader('Subset of Data')
st.dataframe(data.head()) 

# Visualization
st.subheader('Distribution of Anime Scores by Type')
fig, ax = plt.subplots()
sns.boxplot(x='Type', y='Score', data=data, palette='Set2')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.write("""
The visualization above shows the distribution of scores for different types of anime, such as TV series, movies, OVAs, etc. This addresses the question of how scores vary across different anime formats.

**Implications:**

- This analysis can be instrumental for anime creators, marketers, and platforms in understanding what types of anime resonate more with audiences.
- It also provides insights for viewers looking to explore different types of anime, giving them an idea of what to expect in terms of general reception.
""")
