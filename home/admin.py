from django.contrib import admin
from .models import Contact,Work

# Style and customize Admin Dashboard
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date')
    date_hierarchy = 'date'
    actions_on_bottom = True

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title',  'github_link')
    prepopulated_fields = {'slug': ('title',)}






# Register your models here.

admin.site.register(Contact, ContactAdmin)

admin.site.register(Work, WorkAdmin)
