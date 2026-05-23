from pathlib import Path
import pandas as pd
import numpy as np

np.random.seed(42)

# ----- customers -----
n_customers = 20
customers = pd.DataFrame({
    "customer_id": range(1, n_customers + 1),
    "region": np.random.choice(["North", "South", "East", "West", "Central"], n_customers)
})

# ----- orders -----
n_orders = 100
orders = pd.DataFrame({
    "order_id": range(1001, 1001 + n_orders),
    "customer_id": np.random.choice(customers["customer_id"], n_orders),
    "sales": np.random.randint(20, 500, n_orders),
    "profit": np.random.randint(-50, 200, n_orders),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], n_orders)
})

# save files
orders_path = Path("orders.csv")
customers_path = Path("customers.csv")

orders.to_csv(orders_path, index=False)
customers.to_csv(customers_path, index=False)

orders_path, customers_path