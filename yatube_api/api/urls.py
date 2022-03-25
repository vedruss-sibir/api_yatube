from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet

router = SimpleRouter()
router.register("api/v1/posts", PostViewSet)
router.register(
    r"api/v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
router.register("api/v1/groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
