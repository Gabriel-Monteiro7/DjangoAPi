from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
  email = models.EmailField(verbose_name = 'email',unique=True)
  REQUIRED_FIELDS = ['username']
  USERNAME_FIELD = 'email'

  def get_username(self):
    return super().email