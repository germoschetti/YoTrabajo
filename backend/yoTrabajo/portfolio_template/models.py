from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User

# Create your models here.

class Template(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to ='portfolio_template/images')
