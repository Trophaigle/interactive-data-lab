import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

#Quel est le total des ventes par région ?
#SELECT c.region, SUM(o.sales) AS total_sales
#FROM orders o
#JOIN customers c
#ON o.customer_id = c.customer_id
#GROUP BY c.region;

df = orders.merge(customers, on="customer_id")
result = df.groupby("region")["sales"].sum()
print(f"Total sales by region:\n{result}")

#TOP 3 categories les plus rantables
#SELECT category, SUM(profit) AS total_profit
#FROM orders
#GROUP BY category
#ORDER BY total_profit DESC#
#LIMIT 3;

result = orders.groupby("category")["profit"].sum().sort_values(ascending=False).head(3)
print(f"Top 3 most profitable categories:\n{result}")

#Cliens qui ont dépensé plus de 1000 euros
#SELECT customer_id, SUM(sales) AS total_sales
#FROM orders
#GROUP BY customer_id
#HAVING SUM(sales) > 1000;

result = orders.groupby("customer_id")["sales"].sum()
result = result[result > 1000]
print(f"Customers who spent more than 1000 euros:\n{result}")