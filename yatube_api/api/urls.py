from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet

router_v1 = SimpleRouter()
router_v1.register("api/v1/posts", PostViewSet)
router_v1.register(
    r"api/v1/posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment",
)
router_v1.register("api/v1/groups", GroupViewSet)

urlpatterns = [
    path("", include(router_v1.urls)),
    path("api/v1/api-token-auth/", views.obtain_auth_token),
]
