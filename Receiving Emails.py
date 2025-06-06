import imaplib
import email

# Email configuration
imap_server = 'your_imap_server.com'
username = 'your_email@example.com'
password = 'your_password'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)
mail.select('inbox')

# Search for emails and fetch them
result, data = mail.search(None, 'ALL')
email_ids = data[0].split()

for email_id in email_ids:
    result, msg_data = mail.fetch(email_id, '(RFC822)')
    raw_email = msg_data[0][1]
    email_message = email.message_from_bytes(raw_email)
    
    print('Subject:', email_message['subject'])
    print('From:', email_message['from'])

# Close the mailbox
mail.logout()
