from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('work/', views.WorkView.as_view(), name='work'),

    path('home-work/', views.HomeWorkView.as_view(), name='home-work'),
      path('work/<slug>/', views.WorkDetailView.as_view(), name='work-detail'),



]