from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from users.models import User
# Create your models here.
class Presentation(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    content = models.TextField()
    profile_picture = models.ImageField(upload_to='presentation/images', null=True)
    cv = models.FileField(upload_to='presentation/cvs', null=True)
    user = models.ForeignKey(User, on_delete= CASCADE, null=False, unique=True)

    def say_hello(message):
        return message
