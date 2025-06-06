import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'your_smtp_server.com'
smtp_port = 587
sender_email = 'your_email@example.com'
password = 'your_password'
receiver_email = 'receiver@example.com'

# Create the email message
subject = 'Subject of your email'
message = 'This is the body of your email.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print('Email could not be sent. Error:', str(e))
finally:
    server.quit()
