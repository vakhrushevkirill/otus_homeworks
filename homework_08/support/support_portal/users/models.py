from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class UserPortal(AbstractUser):
    age = models.IntegerField(null=True)
