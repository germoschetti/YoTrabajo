from django.contrib import admin
from skills.models import Skill
# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
