from rest_framework.routers import DefaultRouter
from personal_information.api.views import PersonalInformationView

router_PersonalInformation = DefaultRouter()
router_PersonalInformation.register(prefix='personal-information', basename='personal-information', viewset=PersonalInformationView)
