from rest_framework import serializers
from .models import  Contact,Work


class ContactSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'date')



class WorkSerializer(serializers.ModelSerializer):
    class Meta:

        model = Work
        fields = (
            "title",
            "label",
            "overview",
            "image",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
            "image_6",
            "github_link",
            "slug",
        )
