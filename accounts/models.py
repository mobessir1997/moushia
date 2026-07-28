from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        PARENT = 'PARENT', 'Parent',
        ADMIN = 'ADMIN', 'Admin'
    name = models.CharField()
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.PARENT)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}-{self.email}"