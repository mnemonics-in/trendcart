from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    reset_token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email