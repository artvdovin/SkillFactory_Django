from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .tasks import send_notifications

from django.conf import settings

from .models import PostCategory


def send_notifications (preview, pk, title, subscribers):
    html_content = render_to_string (
        'post_created_email.html',
        {
            'text':preview,
            'link':f'{settings.SITE_URL}/news/{pk}'
        }

    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, sender, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers_emails = []
        
        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]
          

        #send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)      
        send_notifications.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)  