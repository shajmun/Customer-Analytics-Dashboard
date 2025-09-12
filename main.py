# Import the libraries we need
import pandas as pd
from sqlalchemy import create_engine

# --- Step 1: Connect to the Database ---
engine = create_engine('sqlite:///Olist_Store.db')


# --- Step 2: Write a Broader SQL Query ---
# This query gets all customer and order data
query = """
SELECT *
FROM olist_customers_dataset
INNER JOIN olist_orders_dataset
ON olist_customers_dataset.customer_id = olist_orders_dataset.customer_id
"""

# --- Step 3: Load Data into Pandas ---
df = pd.read_sql_query(query, engine)


# --- Step 4: Data Cleaning and Feature Engineering ---

# Convert all date columns to datetime objects
for col in ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']:
    df[col] = pd.to_datetime(df[col])

# Calculate shipping time
df['shipping_time'] = df['order_delivered_customer_date'] - df['order_purchase_timestamp']


# --- Step 5: Analysis ---
# filter and analyze
print("Average shipping time for all orders:")
print(df['shipping_time'].mean())

print("\nAverage shipping time for orders before 2017-01-01:")
df_before_2017 = df[df['order_purchase_timestamp'] < '2017-01-01']
print(df_before_2017['shipping_time'].mean())


# --- Step 6: Save the Cleaned Data ---
# Save the full, cleaned dataset for use in Tableau
df.to_csv('cleaned_olist_data.csv', index=False)

print("\nSuccessfully saved cleaned data to cleaned_olist_data.csv")