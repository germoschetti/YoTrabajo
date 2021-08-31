from django.contrib import admin
from portfolio_template.models import Template
# Register your models here.


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'content', 'image']
