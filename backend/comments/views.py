from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers
from . import models as comment_models
from posts import models as post_models

# Create your views here.


class CommentView(APIView):
    serializer_classes = [serializers.CommentSerializer]

    def get(self, request, **kwargs):
        pk = kwargs.get("pk")

        comments = post_models.Post.objects.get(pk=pk).comments.all()

        serializer = serializers.CommentSerializer(comments, many=True)
        print(f"request : {request}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        pk = kwargs.get("pk")
        print("asd")
        post = post_models.Post.objects.get(pk=pk)

        print(f"댓글 POST : {request}")
        print(f"댓글 소유자 : {request.user}")
        print("댓글 게시글", {post})
        print(f"request Data : {request.data}")

        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        pk = kwargs.get("pk")
