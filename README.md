I wrote this script because manually emailing recruiters was killing me. It reads names and emails from a CSV, personalizes the message, and sends it using SMTP. It’s simple, it works, and it saved my sanity (barely).

## How to Use
**1. Clone the Repository:**
```bash
git clone https://github.com/ananyakaligal/Email-Automation.git
cd Email-Automation
```

**2. Prepare Your CSV:**
Create a file named contacts.csv with this format:
```bash
Name,Email
John Doe,johndoe@example.com
Jane Smith,janesmith@example.com
```

**3. Edit the SMTP Configuration:**
**SMTP Configuration:** Update the SMTP server and port based on the email provider you're using. For gmail it is:
```bash
smtp_server = "smtp.gmail.com"
smtp_port = 587
```
**Email Content:** Customize the subject and body of the email:

**4. Run the script**
```bash
python automation.py
```

## Using an App Password
Some email providers, like Gmail, require an App Password instead of your regular password for added security. Here's how to set it up:

**For Gmail:**

**1. Enable 2-Step Verification:**
Go to Google My Account.
Navigate to Security > 2-Step Verification and turn it on.

**2. Generate an App Password:**
Go to Security > App Passwords.
Select Mail as the app and Windows Computer (or any device name).
Generate and copy the 16-character password.

**3. Use It in the Script:**
When the script prompts for your password, paste the App Password instead of your regular email password.
For other providers, search for "App Password for [your email provider]" for specific instructions.
