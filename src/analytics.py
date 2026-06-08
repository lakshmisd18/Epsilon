def get_summary(df):

    return {
        "total_customers": len(df),

        "average_orders": round(
            df["TotalOrders"].mean(), 2
        ),

        "average_spending": round(
            df["TotalSpent"].mean(), 2
        ),

        "average_recency": round(
            df["Recency"].mean(), 2
        )
    }