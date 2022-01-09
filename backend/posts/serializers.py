from rest_framework import serializers
from . import models as post_models
from accounts import models as user_models


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_models.Photo
        fields = ["pk", "file", "caption"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ["pk", "username", "email"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    photo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = post_models.Post
        fields = "__all__"

    def get_photo(self, obj):
        return [PhotoSerializer(i).data for i in obj.photos.all()]
