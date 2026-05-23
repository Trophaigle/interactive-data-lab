# responsable de récupérer les données
import requests

def fetch_products():
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON data as a Python list
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching products: {e}")
        return []  # Return an empty list in case of an error
