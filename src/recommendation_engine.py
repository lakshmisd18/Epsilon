def get_recommendation(segment):

    recommendations = {

        "Premium Customers":
        "Offer VIP discounts and loyalty rewards.",

        "Regular Customers":
        "Cross-sell related products.",

        "Occasional Customers":
        "Send promotional offers.",

        "At Risk Customers":
        "Launch retention campaigns."
    }

    return recommendations.get(
        segment,
        "No recommendation available."
    )