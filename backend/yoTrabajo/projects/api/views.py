from rest_framework.viewsets import ModelViewSet
from projects.api.permissions import IsOwnerOrReadOnly
from projects.api.serializer import ProjectSerializer
from projects.models import Project
from django_filters.rest_framework import DjangoFilterBackend
class ProjectViews(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']