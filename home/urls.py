from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about')
]