import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("online_retail.csv", encoding='latin1')

print(df.head())

df = df.dropna()

df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]

df['Revenue'] = df['Quantity'] * df['UnitPrice']

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Revenue'].sum()

print(monthly_sales)

monthly_sales.plot(figsize=(10,5))

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()