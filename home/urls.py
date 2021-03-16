from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('work/', views.WorkView.as_view(), name='work'),
    path('speaking/', views.SpeakingView.as_view(), name='speaking'),
    path('calendar/', views.CalendarView.as_view(), name='calendar')


]