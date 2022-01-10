from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User

# Create your models here.

class Skill(models.Model):
    title = models.CharField(max_length=255)
    skill_management = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=CASCADE, null=False)
