#transforme API → DataFrame

import pandas as pd
from utils.api import fetch_products

def load_data():
    # Fetch products from the API
    products = fetch_products()
    
    # Convert the list of products to a DataFrame
    df = pd.DataFrame(products)
    
    return df