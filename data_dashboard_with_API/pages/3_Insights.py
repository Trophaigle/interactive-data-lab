import streamlit as st
from data.data_loader import load_data

df = load_data()

most_expensive = df.loc[df['price'].idxmax(), "title"] #idxmax() pour trouver l'index du produit le plus cher, puis on utilise cet index pour accéder au titre du produit avec .loc[]
cheapest = df.loc[df['price'].idxmin(), "title"]

st.write(f"Produit le plus cher: {most_expensive}")
st.write(f"Produit le moins cher: {cheapest}")


