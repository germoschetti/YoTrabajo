from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='portfolio/images')
    repository = models.URLField()
    website = models.URLField(default= '')
