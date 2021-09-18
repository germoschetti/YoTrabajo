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
from django.conf.urls import url
from django.views.static import serve
import os
# views
from users.api.router import RouterUsers
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments
from presentation.api.routes import router_Presentation
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
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'posts')
SITE_ROOT1 = os.path.join(BASE_DIR, 'portfolio_template')
SITE_ROOT2 = os.path.join(BASE_DIR, 'presentation')
SITE_ROOT3 = os.path.join(BASE_DIR, 'projects')
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
    path('api/', include(router_Presentation.urls)),
    path('api/', include(router_skill.urls)),
    path('api/', include(router_project.urls)),
    path('api/', include(router_contact.urls)),
    path('api/', include(router_template.urls)),
    url(r'^posts/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='posts_path'
        ),
    url(r'^portfolio_template/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT1, 'show_indexes': True},
        name='portfolio_template_path'
        ),
    url(r'^presentation/(?P<path>.*)$', serve,
    {'document_root': SITE_ROOT2, 'show_indexes': True},
    name='presentation_path'
    ),
    url(r'^projects/(?P<path>.*)$', serve,
    {'document_root': SITE_ROOT3, 'show_indexes': True},
    name='projects_path'
    ),
]
