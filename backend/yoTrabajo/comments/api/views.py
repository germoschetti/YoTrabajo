from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer, CreateCommentSerializer
from comments.models import Comment
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentsView(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateCommentSerializer
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['post']
    ordering = ['-created_at']


