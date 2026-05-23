import pandas as pd

def add_features(df):
   #decoupage de la colonne 'price' en catégories (intervalles de prix et label les catégories)
    df['price_category'] = pd.cut(df['price'], bins=[0, 50, 100, 200, float('inf')], labels=['Low', 'Medium', 'High', 'Premium'])
    return df