from home.serializers import AboutSerializer, ContactSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import Contact, About

# Create your views here.

class ContactView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer


class AboutView(CreateAPIView):
    serializer_class = AboutSerializer
    queryset = Contact.objects.all()
