from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers
from . import models as comment_models
from posts import models as post_models

# Create your views here.


class UpdateCommentView(APIView):
    def put(self, request, **kwargs):
        post_pk = kwargs.get("pk")
        comment_pk = kwargs.get("comment_pk")

        print(f"게시글 번호 : {post_pk}")
        print(f"댓글 번호 : {comment_pk}")

        post = post_models.Post.objects.get(pk=post_pk)
        print(f"해당 게시글 : {post}")

        if comment_pk is not None:
            comment = comment_models.Comment.objects.get(pk=comment_pk)
            print(f"수정하고자 하는 댓글: {comment}")
            serializer = serializers.CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        comment_pk = kwargs.get("comment_pk")
        if comment_pk is not None:
            comment = comment_models.Comment.objects.get(pk=comment_pk)
            comment.delete()
            return Response("comment delete", status=status.HTTP_200_OK)

        return Response("comment not deleted", status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    serializer_classes = [serializers.CommentSerializer]

    def get(self, request, **kwargs):
        pk = kwargs.get("pk")

        comments = post_models.Post.objects.get(pk=pk).comments.all()

        serializer = serializers.CommentSerializer(comments, many=True)
        print(f"current logged in user : {request.user}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        pk = kwargs.get("pk")
        print("asd")
        post = post_models.Post.objects.get(pk=pk)

        print(f"댓글 POST : {request}")
        print(f"댓글 소유자 : {request.user}")
        print("댓글 게시글", {post})
        print(f"요청받은 데이터 : {request.data}")

        serializer = serializers.CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            print("댓글 저장 완료")
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
