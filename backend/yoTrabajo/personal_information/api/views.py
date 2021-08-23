from rest_framework.viewsets import ModelViewSet
from personal_information.api.permissions import IsOwnerOrReadOnly
from personal_information.api.serializers import PersonalInformationSerializer
from personal_information.models import PersonalInformation
from django_filters.rest_framework import DjangoFilterBackend


class PersonalInformationView(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PersonalInformationSerializer
    queryset = PersonalInformation.objects.all()

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']
