from rest_framework.routers import DefaultRouter
from comments.api.views import CommentsView

router_comments = DefaultRouter()
router_comments.register(prefix='comments', basename='comments', viewset=CommentsView)
