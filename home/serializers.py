from rest_framework import serializers
from .models import Contact, About


class ContactSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'date')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:

        model = About
        fields = ('bio',)