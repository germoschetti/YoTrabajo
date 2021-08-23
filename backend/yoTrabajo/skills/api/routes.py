from rest_framework.routers import DefaultRouter
from skills.api.views import SkillViews

router_skill = DefaultRouter()
router_skill.register(prefix='skills', basename='skills', viewset=SkillViews)
