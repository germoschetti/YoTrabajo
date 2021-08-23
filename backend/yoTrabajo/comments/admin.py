from django.contrib import admin
from comments.models import Comment

@admin.register(Comment)
class Coment(admin.ModelAdmin):
    list_display = ['user', 'created_at']

