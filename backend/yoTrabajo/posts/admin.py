from django.contrib import admin
from posts.models import Post
# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display= ['title', 'category', 'user', 'created_at', 'published']
