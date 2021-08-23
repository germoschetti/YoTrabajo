from categories.models import CategoriesModel
from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategoriesSerializer
from categories.api.permisions import IsAdminOrReadOnly 

from django_filters.rest_framework import DjangoFilterBackend


class CategoriesView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoriesSerializer
    #queryset = CategoriesModel.objects.all()
    queryset = CategoriesModel.objects.filter(published = True)
    #Configuraciones filtrado
    lookup_field = 'slug'

    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['title']