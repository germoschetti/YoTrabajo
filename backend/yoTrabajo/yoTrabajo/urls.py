"""yoTrabajo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# views
from users.api.router import RouterUsers
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments
from personal_information.api.routes import router_PersonalInformation
from skills.api.routes import router_skill
from projects.api.router import router_project
from contact.api.routes import router_contact
from portfolio_template.api.routes import router_template

schema_view = get_schema_view(
    openapi.Info(
        title="YoTrabajo",
        default_version='v1',
        description="Documentacion de la API de YoTrabajo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="germoschetti@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc',
                                        cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include(RouterUsers)),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
    path('api/', include(router_PersonalInformation.urls)),
    path('api/', include(router_skill.urls)),
    path('api/', include(router_project.urls)),
    path('api/', include(router_contact.urls)),
    path('api/', include(router_template.urls)),
]
