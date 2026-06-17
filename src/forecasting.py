def revenue_forecast(df):

    total_revenue = df[
        "TotalSpent"
    ].sum()

    monthly_revenue = (
        total_revenue / 12
    )

    forecast = {

        "30 Days":
        round(monthly_revenue, 2),

        "60 Days":
        round(monthly_revenue * 2, 2),

        "90 Days":
        round(monthly_revenue * 3, 2)
    }

    return forecast