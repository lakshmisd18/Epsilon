def generate_campaign(intent):

    campaigns = {

        "Likely Buyer": {

            "Campaign":
            "VIP Rewards Program",

            "Message":
            "Exclusive 20% discount for loyal customers.",

            "Objective":
            "Increase Repeat Purchases"
        },

        "Potential Buyer": {

            "Campaign":
            "Cross Sell Campaign",

            "Message":
            "Products frequently bought together.",

            "Objective":
            "Increase Basket Size"
        },

        "Needs Engagement": {

            "Campaign":
            "Engagement Campaign",

            "Message":
            "Special offers and personalized deals.",

            "Objective":
            "Increase Activity"
        },

        "Churn Risk": {

            "Campaign":
            "Win Back Campaign",

            "Message":
            "We miss you. Come back and save 30%.",

            "Objective":
            "Customer Retention"
        }
    }

    return campaigns.get(intent)