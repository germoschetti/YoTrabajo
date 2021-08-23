from rest_framework import serializers
from comments.models import Comment
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
   # user = UserSerializer()
   # post = PostSerializer()
    class Meta:

        model = Comment
        fields = ['id','user', 'post', 'created_at', 'content']
