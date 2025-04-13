from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from datetime import timezone, datetime
from .models import Post, Category
from django.conf import settings

import time

  


@shared_task
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

@shared_task
def period_send_notifications():
    #  Your job processing logic here... 
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_add__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscriptions = set(Category.objects.filter(name__in=categories).values_list('subscribers__email',flat=True))
    html_content = render_to_string(
        'news_post_mail.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body = '',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscriptions
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()