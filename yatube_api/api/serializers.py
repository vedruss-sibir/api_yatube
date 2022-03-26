from rest_framework import serializers

from posts.models import Group, Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Comment
        fields = "__all_"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("title",)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Post
        fields = ("id", "text", "author", "image", "pub_date", "group")
