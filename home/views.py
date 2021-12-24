from home.serializers import ContactSerializer, WorkSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from .models import Contact, Work

# Create your views here.

class ContactView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def post(self,request,*args,**kwargs):
        name= request.data.get("name", None)
        email= request.data.get("email", None)
        message= request.data.get("message", None)

        contact = Contact(
            name=name,
            email=email,
            message=message)
        contact.save()
        return Response(status=HTTP_200_OK)

class WorkView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WorkSerializer
    queryset = Work.objects.all()


class WorkDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    lookup_field = "slug"
