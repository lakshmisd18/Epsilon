def answer_query(query, df):

    query = query.lower()

    if "highest revenue" in query:

        segment = (
            df.groupby("Segment")
            ["TotalSpent"]
            .sum()
            .idxmax()
        )

        return (
            f"{segment} generates the highest revenue."
        )

    elif "at risk" in query:

        count = len(

            df[
                df["Intent"]
                ==
                "Churn Risk"
            ]
        )

        return (
            f"{count} customers are at churn risk."
        )

    elif "highest spending" in query:

        customer = df.loc[
            df["TotalSpent"].idxmax()
        ]

        return (
            f"Customer "
            f"{customer['CustomerID']} "
            f"has the highest spending."
        )

    elif "premium" in query:

        return (
            "Recommend loyalty rewards "
            "and VIP campaigns."
        )

    else:

        return (
            "Try asking about revenue, "
            "spending, premium customers, "
            "or at-risk customers."
        )