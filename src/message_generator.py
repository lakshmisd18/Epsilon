def generate_message(customer_name,
                     segment,
                     intent):

    if segment == "Premium Customers":

        return f"""
Hi {customer_name},

As one of our valued premium customers,
we have created an exclusive offer
tailored just for you.

Enjoy VIP benefits today.
"""

    elif segment == "At Risk Customers":

        return f"""
Hi {customer_name},

We noticed you haven't interacted recently.

Come back and enjoy special discounts
created just for you.
"""

    return f"""
Hi {customer_name},

Thank you for being with us.

Check out our latest recommendations.
"""