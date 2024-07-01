from mailersend import MailerSend, Email, Recipient

mailersend = MailerSend(api_key='your_api_key')

def send_email():
    email = Email(
        from_email='your_email@example.com',
        to=['recipient@example.com'],
        subject='Your Subject',
        text='Your plain text content',
        html='<p>Your HTML content</p>'
    )
    response = mailersend.send(email)
    print(response)

send_email()
