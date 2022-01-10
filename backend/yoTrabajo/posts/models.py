from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import CategoriesModel
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')
    content = models.TextField()
    miniature = models.ImageField(upload_to='posts/images')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(CategoriesModel, on_delete=SET_NULL, null=True)


    def __str__(self):
        return self.title
