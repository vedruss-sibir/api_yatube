from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet

router_v1 = SimpleRouter()
router_v1.register(r"posts", PostViewSet, basename="posts")
router_v1.register(r"groups", GroupViewSet, basename="groups")
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
