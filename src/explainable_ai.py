def explain_customer(customer):

    segment = customer["Segment"]

    if segment == "Premium Customers":

        return """
This customer belongs to the Premium Customers segment because
they demonstrate strong purchasing behaviour, high engagement,
and significant contribution to revenue.

The customer is considered highly valuable and is likely to
respond positively to loyalty programs and premium offers.
"""

    elif segment == "At Risk Customers":

        return """
This customer has shown value in the past but recent activity
indicates a risk of disengagement.

The customer has not interacted recently, which increases the
probability of churn.

A personalized win-back campaign is recommended to recover
engagement and retain the customer.
"""

    elif segment == "Regular Customers":

        return """
This customer demonstrates stable purchasing behaviour and
moderate engagement.

The customer is active but has not yet reached premium loyalty
levels.

Targeted promotions and personalized recommendations can help
increase future purchases.
"""

    else:

        return """
This customer interacts occasionally and contributes lower
business value compared to other segments.

Marketing efforts should focus on increasing engagement and
purchase frequency.
"""