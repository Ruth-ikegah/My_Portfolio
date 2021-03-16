from home.serializers import AboutSerializer, CalendarSerializer, ContactSerializer, SpeakingSerializer, WorkSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import Calendar, Contact, About, Speaking, Work

# Create your views here.

class ContactView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer


class AboutView(CreateAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()


class WorkView(CreateAPIView):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

class SpeakingView(CreateAPIView):
    serializer_class = SpeakingSerializer
    queryset = Speaking.objects.all()

class CalendarView(CreateAPIView):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()
