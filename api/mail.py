from django.core.mail import get_connection, EmailMultiAlternatives
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()


def sent_email(subject, message):
    try:
        connection = get_connection()
        connection.open()
        email = EmailMultiAlternatives(
                subject, message, settings.EMAIL_HOST_USER,
                os.getenv('MAIL_LIST').split(), connection=connection)
        email.send()
        connection.close()
    except:
        print('mail error')
