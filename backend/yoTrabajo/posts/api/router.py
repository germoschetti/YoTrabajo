from rest_framework.routers import DefaultRouter
from posts.api.views import PostViews

router_posts = DefaultRouter()
router_posts.register(prefix='posts', basename='posts', viewset=PostViews)
