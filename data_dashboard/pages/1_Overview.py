# Overview business page
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# dossier du script actuel ('pages' ici)
SCRIPT_DIR = os.path.dirname(__file__)

# remonter au dossier racine du projet (si scripts/ est un niveau en dessous)
#('data_dashboard' ici)
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# chemin vers le CSV, va dans data/data.csv depuis 'data_dashboard'
file_path = os.path.join(BASE_DIR, "data", "data.csv")

df = pd.read_csv(file_path)

st.title("Overview")

#KPIs
st.metric("Sales", df["Sales"].sum())
st.metric("Profit", df["Profit"].sum())

# Graph
fig = px.bar(df, x="Category", y="Sales", color="Region")
st.plotly_chart(fig)