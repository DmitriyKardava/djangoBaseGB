import logging
from typing import Dict, Union
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model 
from django.core.mail import send_mail
from django.conf import settings
logger = logging.getLogger(__name__)


settings

@shared_task
def send_feedback_mail(message_form: Dict[str, Union[int, str]]) -> None:
    logger.info(f"Send message: '{message_form}'")
    # model_user = get_user_model()
    # user_obj = model_user.objects.get(pk=message_form["user_id"]) 
    send_mail("TechSupport Help", # subject (title) 
        message_form["message"], # message 
        settings.EMAIL_HOST_USER, # from
        [settings.SUPPORT_EMAIL], # to
        fail_silently=False,
    )
    return None
