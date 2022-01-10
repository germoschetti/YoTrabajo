from rest_framework import serializers
from categories.models import CategoriesModel


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = ['id', 'title', 'slug', 'published']
