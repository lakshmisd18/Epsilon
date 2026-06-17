def detect_intent(text):

    text = text.lower()

    intent_keywords = {

        "Travel": [
            "passport",
            "flight",
            "visa",
            "hotel",
            "travel",
            "bag",
            "luggage",
            "roaming",
            "tour"
        ],

        "Finance": [
            "stock",
            "crypto",
            "investment",
            "loan",
            "bank",
            "forex",
            "mutual fund"
        ],

        "Education": [
            "course",
            "study",
            "exam",
            "learn",
            "college",
            "tutorial",
            "programming",
            "python"
        ],

        "Gaming": [
            "game",
            "gaming",
            "ps5",
            "xbox",
            "pubg",
            "esports"
        ],

        "Shopping": [
            "buy",
            "price",
            "discount",
            "amazon",
            "deal",
            "smartphone",
            "shoes",
            "laptop"
        ]
    }

    for intent, keywords in intent_keywords.items():

        for keyword in keywords:

            if keyword in text:

                return intent

    return "Unknown"


def get_strategy(intent):

    strategies = {

        "Travel": {

            "Products":
            [
                "Travel Insurance",
                "Hotel Packages",
                "Roaming Plans"
            ],

            "Channel":
            "Email + Google Ads"
        },

        "Finance": {

            "Products":
            [
                "Investment Plans",
                "Credit Cards"
            ],

            "Channel":
            "LinkedIn + Email"
        },

        "Education": {

            "Products":
            [
                "Online Courses",
                "Certifications"
            ],

            "Channel":
            "YouTube + Email"
        },

        "Gaming": {

            "Products":
            [
                "Gaming Accessories",
                "Consoles"
            ],

            "Channel":
            "Instagram + YouTube"
        },

        "Shopping": {

            "Products":
            [
                "Coupons",
                "Special Deals"
            ],

            "Channel":
            "Facebook + Email"
        }
    }

    return strategies.get(intent)