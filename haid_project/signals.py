#!/usr/bin/env python
# encoding: utf-8


import logging

import django.dispatch
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver

logger = logging.getLogger(__name__)

oauth_user_login_signal = django.dispatch.Signal(providing_args=['id'])
send_email_signal = django.dispatch.Signal(
    providing_args=['emailto', 'title', 'content'])


@receiver(send_email_signal)
def send_email_signal_handler(sender, **kwargs):
    emailto = kwargs['emailto']
    title = kwargs['title']
    content = kwargs['content']

    msg = EmailMultiAlternatives(
        title,
        content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=emailto)
    msg.content_subtype = "html"

    try:
        result = msg.send()

    except Exception as e:
        logger.error(e)
