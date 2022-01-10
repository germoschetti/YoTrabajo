from rest_framework.viewsets import ModelViewSet
from presentation.api.permissions import IsOwnerOrReadOnly
from presentation.api.serializers import PresentationSerializer
from presentation.models import Presentation
from django_filters.rest_framework import DjangoFilterBackend


class PresentationView(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PresentationSerializer
    queryset = Presentation.objects.all()

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']
