from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Day
from datetime import timedelta

@receiver(user_logged_in)
def create_missing_days_on_login(sender, request, user, **kwargs):
    today = now().date()
    last_login = user.last_login.date() if user.last_login else today
    
    while last_login <= today:
        if not Day.objects.filter(user=user, date=last_login).exists():
            Day.objects.create(user=user, date=last_login)
        last_login += timedelta(days=1)