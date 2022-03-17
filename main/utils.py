from django.conf import settings
from django.core.mail import EmailMessage


def send_email(
    email_subject, message, to_email, from_email=settings.DEFAULT_FROM_EMAIL
):
    email = EmailMessage(email_subject, message, from_email, to=[to_email])
    email.send()
