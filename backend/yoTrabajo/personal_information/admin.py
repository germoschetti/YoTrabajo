from personal_information.models import PersonalInformation
from django.contrib import admin
from personal_information.models import PersonalInformation

# Register your models here.
@admin.register(PersonalInformation)
class Personal_Information(admin.ModelAdmin):
    pass
