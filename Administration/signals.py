from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser


@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    if sender.name == 'Administration':
        if not CustomUser.objects.filter(username=settings.DEFAULT_USERNAME).exists():
            CustomUser.objects.create_superuser(
                username=settings.DEFAULT_USERNAME,
                password=settings.DEFAULT_PASSWORD,
                role='SUPER_ADMINISTRADOR'
            )
