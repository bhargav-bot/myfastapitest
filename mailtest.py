from mailersend import emails

# Replace 'API key here' with your actual MailerSend API key
api_key = "mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec"

# Initialize the NewEmail client
mailer = emails.NewEmail(api_key)

# Define email parameters directly
mail_from = {
    "email": "760041bp@gmail.com",  # Your email address
}

recipients = [
    {
        "email": "bhargavp19082002@gmail.com",  # Recipient's email address
    }
]

# Set email attributes
mailer.set_mail_from(mail_from)
mailer.set_mail_to(recipients)
mailer.set_subject("Hello from MailerSend!")
mailer.set_html_content("<p>This is the HTML content of the email.</p>")
mailer.set_plaintext_content("This is the plain text content of the email.")

# Send the email
response = mailer.send()

# Check the response
if response.status_code == 200:
    print("Email sent successfully!")
else:
    print(f"Failed to send email. Status code: {response.status_code}")

from mailersend import emails

api_key = "API key here"

mailer = emails.NewEmail(api_key)

# define an empty dict to populate with mail values
mail_body = {}

mail_from = {
    "email": "760041bp@gmail.com",  # Your email address
}

recipients = [
    {
        "email": "bhargavp19082002@gmail.com",  # Recipient's email address
    }
]


mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)
mailer.set_subject("Hello!", mail_body)
mailer.set_html_content("This is the HTML content", mail_body)
mailer.set_plaintext_content("This is the text content", mail_body)


# using print() will also return status code and data
mailer.send(mail_body)