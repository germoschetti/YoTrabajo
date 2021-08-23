from django.contrib import admin
from contact.models import Contact
# Register your models here.

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    pass
