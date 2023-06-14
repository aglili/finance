from resend import Resend
import os
from dotenv import load_dotenv
import resend

load_dotenv()
resend.api_key = os.getenv("Resend_API_KEY")

def send_email_to_user(email, subject, message):
    r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": subject,
        "html": message
    })
