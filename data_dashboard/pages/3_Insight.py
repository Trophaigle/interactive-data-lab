#interpretation page with business insights
import streamlit as st
import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SCRIPT_DIR)
file_path = os.path.join(BASE_DIR, "data", "data.csv")

df = pd.read_csv(file_path)

st.title("Business Insight")

top_region= df.groupby("Region")["Sales"].sum().idxmax()
best_category = df.groupby("Category")["Profit"].sum().idxmax()

st.write(f"Top Region: {top_region}")
st.write(f"Best Category: {best_category}")