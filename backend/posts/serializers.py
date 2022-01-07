from rest_framework import serializers
from . import models as post_models
from accounts import models as user_models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ["pk", "username", "email"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = post_models.Post
        fields = "__all__"
