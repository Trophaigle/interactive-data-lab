#Machie learning page for customer segmentation using KMeans clustering
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import plotly.express as px
import os

SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SCRIPT_DIR)
file_path = os.path.join(BASE_DIR, "data", "data.csv")

df = pd.read_csv(file_path)

st.title("Customer Segmentation")

#données → nettoyage → normalisation → clustering
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")), #remplacer les valeur manquantes par la moyenne
    ("scaler", StandardScaler()), #normaliser les données pour que KMeans fonctionne mieux
    ("model", KMeans(n_clusters=3, random_state=42))  #appliquer KMeans pour segmenter les clients en 3 groupes
    ])

# clustering
df["cluster"] = pipeline.fit_predict(df[["Sales", "Profit"]])

# visualisation
fig = px.scatter(df, x="Sales", y="Profit", color="cluster")
st.plotly_chart(fig)

st.write("Moyennes par cluster :")
#calculer les moyennes de ventes et profits pour chaque cluster pour comprendre les caractéristiques de chaque segment
clusters_stats = df.groupby("cluster")[["Sales", "Profit"]].mean() #moyennes de ventes et profits par cluster
st.write(clusters_stats)

# calculer un score pour chaque cluster en combinant les ventes et les profits
clusters_stats["score"] = clusters_stats["Sales"] + clusters_stats["Profit"]

#trier les clusters par score pour les interpréter plus facilement
clusters_stats = clusters_stats.sort_values("score", ascending=False)
st.write("Clusters triés par score :")
st.write(clusters_stats)

#associer un nom à chaque cluster pour une meilleure interprétation
mapping = {
    clusters_stats.index[0]: "High Value",
    clusters_stats.index[1]: "Medium Value",
    clusters_stats.index[2]: "Low Value"    
}

df["cluster_name"] = df["cluster"].map(mapping) #ajouter une colonne avec les noms des clusters pour une visualisation plus intuitive (au lieu de 0,1,2 on aura High Value, Medium Value, Low Value)

fig = px.scatter(df, x="Sales", y="Profit", color="cluster_name", title="Customer Segmentation")
st.plotly_chart(fig)

