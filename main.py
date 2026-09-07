import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def send_email_with_anti_auto_reply_headers():
    """
    Sends an email with headers designed to suppress automatic replies.
    """
    # --- Configuration (set these as environment variables or replace directly) ---
    # For Gmail, use 'smtp.gmail.com' and port 587. You might need an 'App Password'
    # if 2-Factor Authentication is enabled for your Google account.
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com") # e.g., smtp.gmail.com
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your_email@example.com")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "your_password")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "recipient@example.com")

    if not all([SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL]):
        print("Error: Please set SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD, and RECIPIENT_EMAIL environment variables.")
        print("Example:")
        print("  export SMTP_SERVER='smtp.gmail.com'")
        print("  export SENDER_EMAIL='your_email@gmail.com'")
        print("  export SENDER_PASSWORD='your_app_password' # Or regular password if 2FA is off")
        print("  export RECIPIENT_EMAIL='test_recipient@example.com'")
        return

    subject = "Test Email with Anti-Auto-Reply Headers"
    body = """
    Hello,

    This email contains special headers designed to prevent automatic replies
    (like Out-of-Office messages). You should not receive an auto-reply from this email.

    Best regards,
    Sender
    """

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = formataddr((str(Header('Example Sender', 'utf-8')), SENDER_EMAIL))
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = Header(subject, 'utf-8')

    # --- Key headers to prevent automatic replies ---
    # 'Precedence: bulk' is a standard header indicating a mass mailing.
    # Mail servers often use this to suppress auto-replies and other automated processing.
    msg['Precedence'] = 'bulk'
    # 'X-Auto-Response-Suppress: All' is a Microsoft-specific header widely adopted.
    # It explicitly tells Exchange servers (and others that respect it) not to send
    # auto-replies (e.g., Out-of-Office, Delivery Reports, Non-Delivery Reports).
    msg['X-Auto-Response-Suppress'] = 'All'
    # Other possible values for X-Auto-Response-Suppress include: OOF, DR, NDR, AutoReply, RN, SN

    try:
        print(f"Attempting to connect to {SMTP_SERVER}:{SMTP_PORT}...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully with anti-auto-reply headers!")
        print(f"Check recipient '{RECIPIENT_EMAIL}' for the email and verify no auto-reply was sent.")
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP authentication failed. Check your email and password.")
        print("For Gmail, ensure you're using an 'App Password' if 2FA is enabled.")
    except smtplib.SMTPConnectError as e:
        print(f"Error: Could not connect to SMTP server. Check server address and port. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_email_with_anti_auto_reply_headers()
