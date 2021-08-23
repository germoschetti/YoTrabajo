from rest_framework import serializers
from portfolio_template.models import Template

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'user', 'title', 'content', 'image']
