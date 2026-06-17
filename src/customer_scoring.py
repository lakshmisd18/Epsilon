def calculate_customer_score(row):

    spending_weight = (
        min(row["TotalSpent"] / 5000, 1)
        * 50
    )

    order_weight = (
        min(row["TotalOrders"] / 20, 1)
        * 30
    )

    recency_weight = (
        max(
            0,
            (365 - row["Recency"]) / 365
        )
        * 20
    )

    return round(
        spending_weight
        + order_weight
        + recency_weight,
        2
    )


def assign_tier(score):

    if score >= 80:
        return "Platinum"

    elif score >= 60:
        return "Gold"

    elif score >= 40:
        return "Silver"

    else:
        return "Bronze"


def add_customer_scoring(df):

    df["CustomerScore"] = df.apply(
        calculate_customer_score,
        axis=1
    )

    df["Tier"] = df[
        "CustomerScore"
    ].apply(
        assign_tier
    )

    return df