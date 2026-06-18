from twilio.rest import Client

ACCOUNT_SID = "ACa87b158b2d50e76ae455a7b511498300"
AUTH_TOKEN = "a7640073e8ef8ce61f46d3d5da2115df"

client = Client(
    ACCOUNT_SID,
    AUTH_TOKEN
)

def send_sms(
    phone,
    message
):

    client.messages.create(
        body=message,
        from_="+123456789",   # Twilio number
        to=phone
    )

def send_whatsapp(
    phone,
    message
):

    client.messages.create(
        body=message,
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{phone}"
    )