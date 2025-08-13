import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env
load_dotenv()

# Fetch variables from environment
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
messaging_service_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")
recipient_number = os.getenv("RECIPIENT_NUMBER")

# Validate all required variables
missing_vars = [
    var_name for var_name, value in {
        "TWILIO_ACCOUNT_SID": account_sid,
        "TWILIO_AUTH_TOKEN": auth_token,
        "TWILIO_MESSAGING_SERVICE_SID": messaging_service_sid,
        "RECIPIENT_NUMBER": recipient_number
    }.items() if not value
]

if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    messaging_service_sid=messaging_service_sid,
    body="Ahoy 👋",
    to=recipient_number #type: ignore
)

print(f"Message sent with SID: {message.sid}")
