from django.contrib import admin
from presentation.models import Presentation
# Register your models here.
@admin.register(Presentation)
class Presentation(admin.ModelAdmin):
    list_display=['id', 'name']
    pass
