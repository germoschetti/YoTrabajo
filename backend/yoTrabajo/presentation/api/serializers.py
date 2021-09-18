from rest_framework import serializers
from presentation.models import Presentation

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ['id', 'user', 'name', 'last_name', 'content']

