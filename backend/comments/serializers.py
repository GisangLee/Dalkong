from rest_framework import serializers
from posts.serializers import AuthorSerializer
from posts import models as post_models
from . import models as comment_models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_models.Post
        fields = ["pk"]


class CommentSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    def create(self, validated_data):
        print(f"댓글 생성 데이터 : {validated_data}")
        comment = comment_models.Comment.objects.create(**validated_data)
        comment.save()
        return comment

    class Meta:
        model = comment_models.Comment
        fields = "__all__"
