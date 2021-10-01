from .models import *
from rest_framework import serializers


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class CuratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curator
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    competence = CompetenceSerializer
    contacts = ContactSerializer
    resource = ResourceSerializer
    curator = CuratorSerializer

    class Meta:
        model = Volunteer
        fields = '__all__'
