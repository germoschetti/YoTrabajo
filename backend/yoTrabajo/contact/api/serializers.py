from rest_framework import serializers
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'linkedin', 'github', 'hotmail', 'gmail', 'wsp', 'twitter']
