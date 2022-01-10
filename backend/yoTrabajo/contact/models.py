from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, unique=True)
    linkedin = models.URLField(default='')
    github = models.URLField(default='')
    hotmail = models.EmailField(default='')
    gmail = models.EmailField(default='')
    wsp = models.IntegerField(default=0)
    twitter = models.URLField(default='')
