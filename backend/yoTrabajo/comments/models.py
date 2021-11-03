from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from users.models import User
from posts.models import Post
# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE , null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

