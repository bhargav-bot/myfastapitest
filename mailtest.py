from mailersend import emails

# Replace 'API key here' with your actual MailerSend API key
api_key = "API key here"

# Initialize the NewEmail client
mailer = emails.NewEmail(api_key)

# Define email parameters directly
mailer.set_mail_from({
    "name": "Your Name",
    "email": "your@domain.com",
})

mailer.set_mail_to([
    {
        "name": "Your Client",
        "email": "your@client.com",
    }
])

mailer.set_subject("Hello!")

mailer.set_html_content("This is the HTML content")

mailer.set_plaintext_content("This is the text content")

mailer.set_reply_to([
    {
        "name": "Name",
        "email": "reply@domain.com",
    }
])

# Send the email
response = mailer.send()

# Check the response
if response.status_code == 200:
    print("Email sent successfully!")
else:
    print(f"Failed to send email. Status code: {response.status_code}")
