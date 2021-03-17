from django.contrib import admin
from .models import Calendar, Contact, About, Speaking, Work

# Style and customize Admin Dashboard
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'date')

# Register your models here.
 
admin.site.register(Contact, ContactAdmin)
admin.site.register(About)
admin.site.register(Work)
admin.site.register(Speaking)
admin.site.register(Calendar)
