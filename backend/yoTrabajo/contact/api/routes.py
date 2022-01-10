from rest_framework.routers import DefaultRouter
from contact.api.views import ContactViews

router_contact = DefaultRouter()
router_contact.register(prefix='contact', basename='contact', viewset=ContactViews)
