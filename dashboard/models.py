from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photos = models.ImageField(upload_to="Users/", blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)