from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_email(self,message):
    send_mail(
        "Message from portfolio Website",
        message,
        settings.EMAIL_HOST_USER,
        ['yahyarehman57@gmail.com']
    )
    return "Done"