import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading dataset...")

df = pd.read_excel(
    "data/Online Retail.xlsx"
)

df = df.dropna(
    subset=["CustomerID"]
)

df = df[
    (df["Quantity"] > 0)
    &
    (df["UnitPrice"] > 0)
]

df["TotalAmount"] = (
    df["Quantity"]
    *
    df["UnitPrice"]
)

print("Creating customer features...")

customer_df = (
    df.groupby("CustomerID")
    .agg(
        {
            "InvoiceNo":"nunique",
            "Quantity":"sum",
            "TotalAmount":"sum"
        }
    )
    .reset_index()
)

customer_df.columns = [
    "CustomerID",
    "TotalOrders",
    "TotalQuantity",
    "TotalSpent"
]

latest_date = (
    df["InvoiceDate"]
    .max()
)

customer_df["Recency"] = (
    latest_date
    -
    df.groupby("CustomerID")
    ["InvoiceDate"]
    .max()
).dt.days.values

print("Running KMeans...")

X = customer_df[
    [
        "TotalSpent",
        "TotalOrders",
        "Recency"
    ]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

customer_df["Cluster"] = (
    kmeans.fit_predict(X_scaled)
)

segment_map = {
    0:"Premium Customers",
    1:"Regular Customers",
    2:"Occasional Customers",
    3:"At Risk Customers"
}

customer_df["Segment"] = (
    customer_df["Cluster"]
    .map(segment_map)
)

customer_df.to_csv(
    "data/segmented_customers.csv",
    index=False
)

print("DONE")
print(customer_df.head())