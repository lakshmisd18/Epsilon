def recommend_channel(age_group, intent, segment):

    if intent == "Churn Risk":
        return "SMS"

    elif intent == "Likely Buyer":
        return "Instagram + Email"

    elif intent == "Potential Buyer":
        return "Facebook"

    else:
        return "Email"


def recommend_time(age_group):

    if age_group == "18-24":
        return "7 PM - 10 PM"

    elif age_group == "25-39":
        return "6 PM - 9 PM"

    elif age_group == "40-54":
        return "12 PM - 2 PM"

    else:
        return "9 AM - 11 AM"