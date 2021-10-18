from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'user', 'title', 'description', 'image', 'repository', 'website' ]
