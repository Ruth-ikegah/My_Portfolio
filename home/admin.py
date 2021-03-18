from django.contrib import admin
from .models import Calendar, Contact, About, Speaking, Work

# Style and customize Admin Dashboard
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'date')
    date_hierarchy = 'date'
    actions_on_bottom = True

class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'problem_statement', 'image', 'image_1', 'image_2', 'live_site', 'github_link')

class SpeakingAdmin(admin.ModelAdmin):
    list_display = ('name', 'abstract', 'image', 'slide_link', 'video_link')

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('talk_title', 'location', 'date', 'register_link')




# Register your models here.
 
admin.site.register(Contact, ContactAdmin)
admin.site.register(About)
admin.site.register(Work, WorkAdmin)
admin.site.register(Speaking, SpeakingAdmin)
admin.site.register(Calendar, CalendarAdmin)
