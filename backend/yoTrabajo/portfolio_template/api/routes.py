from rest_framework.routers import DefaultRouter
from portfolio_template.api.views import TemplateViews

router_template = DefaultRouter()
router_template.register(prefix='template', basename='template', viewset=TemplateViews)
