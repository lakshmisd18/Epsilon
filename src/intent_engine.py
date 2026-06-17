def predict_intent(row):

    total_spent = row["TotalSpent"]
    total_orders = row["TotalOrders"]
    recency = row["Recency"]

    if total_spent > 3000 and recency < 30:
        return "Likely Buyer"

    elif total_orders >= 5 and recency < 90:
        return "Potential Buyer"

    elif recency > 180:
        return "Churn Risk"

    else:
        return "Needs Engagement"


def add_intent(df):

    df["Intent"] = df.apply(
        predict_intent,
        axis=1
    )

    return df