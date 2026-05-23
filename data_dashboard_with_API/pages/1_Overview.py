import streamlit as st
import plotly.express as px
from data.data_loader import load_data
from features.feature_engineering import add_features

df = add_features(load_data()) #ajout des features

st.title("Overview des produits")

st.metric("Total Products: ", len(df))
st.metric("Average Price: ", f"${df['price'].mean():.2f}")

fig = px.histogram(df, x='price', color ="price_category", title='Distribution des catégories de prix')
st.plotly_chart(fig)