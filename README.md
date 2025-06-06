# Python-Email-Automation-Send-and-Receive-Emails
This repository contains simple Python scripts demonstrating how to **send** and **receive** emails programmatically using standard Python libraries.

- **Send Email**: Use the `smtplib` library to send emails from your account via SMTP.
- **Receive Email**: Use the `imaplib` library to connect to your email inbox via IMAP and fetch emails.

## Features

- Send plain text emails with customizable subject and message.
- Connect securely to SMTP and IMAP servers.
- Fetch and display email subjects and sender details.
- Basic examples designed for easy customization and integration.

## Prerequisites

- Python 3.x installed
- Access to an email account with SMTP and IMAP enabled
- Replace placeholders (`your_email@example.com`, `your_password`, etc.) with your actual credentials.

## Usage

### Sending Email

Update the SMTP server settings, your email, password, and receiver email in the `send_email.py` script, then run:

```bash
python send_email.py
