import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, password):
    # Set up the email parameters
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

# Example usage
sender_email = 'rugved.221235.co@mhssce.ac.in'
receiver_email = 'rugvedsacpatil2004@gmail.com'
subject = 'Test Email'
body = 'Hello, this is a test email sent from Python!'
password = 'Rpegy kbat twqa xsnl'

send_email(sender_email, receiver_email, subject, body, password)
