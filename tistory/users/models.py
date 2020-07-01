from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=True, null=True,)
    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     return super().save(*args, **kwargs)
