import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(
        unique=True,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )

    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()

    class Meta:
        ordering = ("created_date",)
