import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("superstore.csv")


st.title("📊 Sales Dashboard")

#KPI, indicateur clé (somme des ventes ici)
st.metric("Total Sales", df["Sales"].sum())

#Graph
fig = px.bar(df, x="Category", y="Sales", color="Region")
st.plotly_chart(fig) #Envoie le graphique dans ton app Streamlit

#table
st.dataframe(df) #DataFrame complet sous forme de tableau interactif

#run in terminal: streamlit run app.py