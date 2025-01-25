import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass  # For securely inputting passwords
import pandas as pd  # For reading the CSV file
import time  # To add delay between emails

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body, smtp_server, smtp_port):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {e}")

# Load contacts from a CSV file
def load_contacts(file_path):
    try:
        contacts = pd.read_csv(file_path)
        print(f"Loaded {len(contacts)} contacts from {file_path}")
        return contacts
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return pd.DataFrame()

# Main script
if __name__ == "__main__":
    # Prompt for sender credentials
    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")  # Hides password input

    # Email configuration
    smtp_server = "smtp.gmail.com"  # Gmail SMTP server
    smtp_port = 587  # Use TLS encryption
    email_subject = "Hello {Name}"  # Subject template
    email_body = (
        "Dear {Name},\n\n"
        "This is a personalized test email sent from the email automation script.\n\n"
        "Best regards,\nYour Script"
    )  # Body template

    # Load contacts from a CSV file
    csv_file = input("Enter the path to your CSV file (e.g., contacts.csv): ")
    contacts = load_contacts(csv_file)

    # Send emails to all contacts
    if not contacts.empty:
        for _, row in contacts.iterrows():
            try:
                # Personalize the email
                recipient_email = row['Email']
                recipient_name = row['Name']
                subject = email_subject.format(Name=recipient_name)
                body = email_body.format(Name=recipient_name)

                # Send the email
                send_email(
                    sender_email,
                    sender_password,
                    recipient_email,
                    subject,
                    body,
                    smtp_server,
                    smtp_port,
                )

                # Pause between emails to avoid server limits
                time.sleep(1)  # Adjust delay as needed
            except KeyError as e:
                print(f"Missing data in row: {row}. Error: {e}")
            except Exception as e:
                print(f"Error sending email to {row.get('Email', 'Unknown')}: {e}")
