from mailersend import emails

# Replace 'API key here' with your actual MailerSend API key
api_key = "mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec"

# Initialize the NewEmail client
mailer = emails.NewEmail(api_key)

message = "hello i amn trsfdggsf"

# Define email parameters directly
mailer.set_mail_from({
    "name": "Your Name",
    "email": "760041bp@gmail.com",

})

mailer.set_mail_to([
    {
        "name": "Your Client",
        "email": "bhargavp19082002@gmail.com",
    }
])

mailer.set_subject("Hello!")

mailer.set_html_content("This is the HTML content")

mailer.set_plaintext_content("This is the text content")

mailer.set_reply_to([
    {
        "name": "Name",
        "email": "bhargavp.0802@gmail.com",
    }
])

# Send the email
response = mailer.send()

# Check the response
if response.status_code == 200:
    print("Email sent successfully!")
else:
    print(f"Failed to send email. Status code: {response.status_code}")
