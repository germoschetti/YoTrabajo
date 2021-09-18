from rest_framework.routers import DefaultRouter
from presentation.api.views import PresentationView

router_Presentation = DefaultRouter()
router_Presentation.register(prefix='presentation', basename='presentation', viewset=PresentationView)
