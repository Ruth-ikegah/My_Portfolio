from rest_framework import serializers
from .models import Calendar, Contact, About, Speaking, Work


class ContactSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contact
        fields = ('name', 'email', 'subject', 'message', 'date')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:

        model = About
        fields = ('bio',)


class WorkSerializer(serializers.ModelSerializer):
    class Meta:

        model = Work
        fields = ('name', 'description', 'problem_statement', 'image', 'image_1', 'image_2', 'live_site', 'github_link')


class SpeakingSerializer(serializers.ModelSerializer):
    class Meta:

        model = Speaking
        fields = ('name', 'abstract', 'image', 'slide_link', 'video_link')


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:

        model = Calendar
        fields = ('talk_title', 'location', 'date', 'register_link')