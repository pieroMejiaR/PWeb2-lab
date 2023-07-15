from django.core.mail import EmailMessage

def send_email(subject, message, from_email, recipient_list):
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()
