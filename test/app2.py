import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import streamlit as st

################### DATA #########################

df = pd.read_csv("superstore.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce") #concert date format
df = df.dropna(subset=["Order Date"]) #Supprime toutes les lignes où la date de commande est manquante

############## SEGMENTATION ###################

features = df[["Sales", "Profit"]]

scaler = StandardScaler()

X = scaler.fit_transform(features)

model = KMeans(n_clusters=3, random_state=42)
df["cluster"] = model.fit_predict(X) #rajoute colonne cluster

############## SideBAR Filter ################

st.sidebar.title("Filters")

region = st.sidebar.selectbox("Region", df["Region"].unique()) #unique pour eviter doublons
category = st.sidebar.selectbox("Category", df["Category"].unique())

filtered_df = df[ #Garder uniquement ce qui correspond à la region et catégorie selectionnées
    (df["Region"] == region) &
    (df["Category"] == category)
]

################## KPIs #######################

st.title("Sales Dashboard (Pro Level)")

st.metric("Total Sales", round(filtered_df["Sales"].sum(), 2)) #total des ventes selon tes filtres (région, catégorie, etc.) et arrondi à 2 chiffres après la virgule
st.metric("Total Profit", round(filtered_df["Profit"].sum(), 2))
st.metric("Orders", len(filtered_df))

################# CHARTS ###################

fig1 = px.bar(filtered_df, x="Sub-Category", y="Sales", color="cluster")
st.plotly_chart(fig1)

fig2 = px.scatter(
    filtered_df,
    x= "Sales",
    y = "Profit",
    color="cluster",
    title="Cutomer Segmentation"
)
st.plotly_chart(fig2)

#################### DATA TABLE ##################"
st.dataframe(filtered_df)

top_region = df.groupby("Region")["Sales"].sum().idxmax() #idxmax: index (nom de Region) avec la plus grande valeur (Sales) - different de head(1) qui renvoie un ligne complete
best_category = df.groupby("Category")["Profit"].sum().idxmax()

st.subheader("🧠 Business Insights")

st.write(f"Top Region: {top_region}")
st.write(f"Most profitable category: {best_category}")


