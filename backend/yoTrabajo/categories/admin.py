from django.contrib import admin
from categories.models import CategoriesModel
# Register your models here.

@admin.register(CategoriesModel)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=['title', 'published']