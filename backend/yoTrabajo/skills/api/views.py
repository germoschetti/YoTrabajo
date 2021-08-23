from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, filterset
from skills.api.serializers import SkillSerializer
from skills.models import Skill
from skills.api.permission import IsOwnerOrReadOnly

class SkillViews(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']