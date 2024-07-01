from mailersend import MailerSend, Email, Recipient

mailersend = MailerSend(api_key='mlsn.43f1eaa97a620bfdb525476088b80d3c481a15d12a5e50b708bf34e00ff9eaec')

def send_email():
    email = Email(
        from_email='bhargavp19082002@gmail.com',
        to=['760041bp@gmail.com'],
        subject='Your Subject',
        text='Your plain text content',
        html='<p>Your HTML content</p>'
    )
    response = mailersend.send(email)
    print(response)

send_email()
