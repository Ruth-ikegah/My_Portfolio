from rest_framework import serializers
from .models import  Contact,Work


class ContactSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'date')



class WorkSerializer(serializers.ModelSerializer):
    class Meta:

        model = Work
        fields = ('name', 'description', 'problem_statement', 'image', 'image_1', 'image_2', 'live_site', 'github_link')
