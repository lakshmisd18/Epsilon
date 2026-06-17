def calculate_health_score(row):

    spending_score = min(
        row["TotalSpent"] / 5000,
        1
    ) * 40

    order_score = min(
        row["TotalOrders"] / 20,
        1
    ) * 30

    recency_score = max(
        0,
        (365 - row["Recency"]) / 365
    ) * 30

    return round(
        spending_score
        + order_score
        + recency_score,
        2
    )


def health_status(score):

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Healthy"

    elif score >= 40:
        return "At Risk"

    return "Critical"


def add_health_metrics(df):

    df["HealthScore"] = df.apply(
        calculate_health_score,
        axis=1
    )

    df["HealthStatus"] = df[
        "HealthScore"
    ].apply(
        health_status
    )

    return df