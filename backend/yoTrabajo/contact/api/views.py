from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from contact.api.serializers import ContactSerializer
from contact.models import Contact
from contact.api.permission import IsOwnerOrReadOnly


class ContactViews(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['user']
