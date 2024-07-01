import mailersend
from mailersend import constants,emails

from mailersend.activity import Activity

mailer = mailersend(api_key='mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec')

# Compose your email details
subject = "Subject"
text = "Greetings from the team, you got this message through MailerSend."
html = "<p>Greetings from the team, you got this message through MailerSend.</p>"

# Define your sender email address
my_mail = "760041bp@gmail.coom"

# Define your list of recipients
subscriber_list = [
   'bhargavp19082002@gmail.com'
]

# Create an Email instance
email = emails(
    from_email=my_mail,
    to=subscriber_list,
    subject=subject,
    text=text,
    html=html
)

# Send the email
response = mailer.send(email)

# Check the response
if response.status_code == 200:
    print("Email(s) sent successfully!")
else:
    print(f"Failed to send email(s). Status code: {response.status_code}")