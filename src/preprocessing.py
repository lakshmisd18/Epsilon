import pandas as pd

print("Loading dataset...")

df = pd.read_excel(
    "data/Online Retail.xlsx"
)

print("Original Shape:", df.shape)

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

print("Cleaned Shape:", df.shape)

print(df.head())