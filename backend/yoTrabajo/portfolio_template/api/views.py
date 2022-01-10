from rest_framework.viewsets import ModelViewSet
from portfolio_template.api.serializers import TemplateSerializer
from portfolio_template.models import Template
from portfolio_template.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class TemplateViews(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']