

from mailersend import emails

api_key = "mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec"

mailer = emails.NewEmail(api_key)

# define an empty dict to populate with mail values
mail_body = {"760041bp@gmail.com"}

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
d= mailer.send(mail_body)
print(d)