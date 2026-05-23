import streamlit as st
from data.data_loader import load_data
from features.feature_engineering import add_features

st.title("Data Dashboard avec API")

@st.cache_data #load en cache
def get_data():
    df = load_data()
    df = add_features(df)
    return df

df = get_data()

st.write("Data loaded from API:")
st.dataframe(df.head())

