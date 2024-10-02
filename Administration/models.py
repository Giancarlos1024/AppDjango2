from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('SUPER_ADMINISTRADOR', 'super_administrador'),
        ('ABOGADO', 'abogado'),
    ]

    role = models.CharField(max_length=19, choices=ROLE_CHOICES, default='ABOGADO')

    def __str__(self):
        return self.username
