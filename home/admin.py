from django.contrib import admin
from .models import Calendar, Contact, About, Speaking, Work

# Register your models here.

admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Work)
admin.site.register(Speaking)
admin.site.register(Calendar)
