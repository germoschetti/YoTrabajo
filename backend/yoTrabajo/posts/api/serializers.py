from posts.models import Post
from rest_framework import serializers
from users.api.serializers import UserSerializer
from categories.api.serializers import CategoriesSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategoriesSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'miniature', 'created_at', 'published', 'user', 'category']
