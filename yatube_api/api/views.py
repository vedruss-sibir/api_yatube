from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from posts.models import Post, User, Group
from .serializers import (
    PostSerializer,
    CommentSerializer,
    UserSerializer,
    GroupSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs.get("post_id")
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("нет доступа")
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("нет доступа")
        super(CommentViewSet, self).perform_destroy(instance)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("нет доступа")
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("нет доступа")
        super(PostViewSet, self).perform_destroy(instance)
