from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from users.models import User
# Create your models here.
class PersonalInformation(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete= CASCADE, null=False, unique=True)
