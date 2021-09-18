from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to ='projects/images')
    repository = models.URLField()
    website = models.URLField(default= '')
