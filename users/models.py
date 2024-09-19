from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    city = models.CharField("Город", max_length=100)

    def __str__(self) -> str:
        return self.username
