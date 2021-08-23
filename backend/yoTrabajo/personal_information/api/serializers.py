from rest_framework import serializers
from personal_information.models import PersonalInformation

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = ['id', 'user', 'name', 'last_name', 'content']

