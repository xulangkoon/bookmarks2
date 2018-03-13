from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# 扩展User model中的字段，加入了user, date_of_birth, photo这些字段
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)