from rest_framework.routers import DefaultRouter
from projects.api.views import ProjectViews

router_project = DefaultRouter()
router_project.register(prefix='proyect', basename='project', viewset=ProjectViews)
