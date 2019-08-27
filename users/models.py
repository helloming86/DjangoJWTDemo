from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    avatar = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)
    mobile = models.CharField(unique=True, max_length=11)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return "Profile for user {}".format(self.user.username)
