from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.


class Article(models.Model):
    """docstring for Article"""
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    likes = models.IntegerField(default=1)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token, created = Token.objects.get_or_create(user=instance)
