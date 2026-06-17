def predict_conversion(segment):

    conversion_rates = {

        "Premium Customers": 18,

        "Regular Customers": 10,

        "Occasional Customers": 5,

        "At Risk Customers": 2
    }

    return conversion_rates.get(
        segment,
        5
    )


def predict_roi(segment):

    roi = {

        "Premium Customers": 250,

        "Regular Customers": 150,

        "Occasional Customers": 90,

        "At Risk Customers": 40
    }

    return roi.get(
        segment,
        50
    )