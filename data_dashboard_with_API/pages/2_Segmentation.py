import streamlit as st
import sklearn.cluster as cluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from data.data_loader import load_data
import plotly.express as px

df = load_data()

df["rating_count"] = df["rating"].apply(lambda x: x["count"])

X = df[["price"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model= KMeans(n_clusters=4, random_state=42)
df['cluster'] = model.fit_predict(X_scaled)

fig = px.scatter(df, x='price', y='rating_count', color='cluster', title='Segmentation des produits par prix')
st.write(df.columns)
st.plotly_chart(fig)