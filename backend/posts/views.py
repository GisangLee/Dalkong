from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models as post_models
from . import serializers
from rest_framework.permissions import AllowAny

# Create your views here.


class UpdatePostView(APIView):
    def error(self):
        return status.HTTP_400_BAD_REQUEST

    def put(self, request, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            post = get_object_or_404(post_models.Post, pk=pk)
            print(f"post is {post.author.pk}")
            print(f"user: {request.user}")

            if post.author.pk == request.user.pk:
                serializer = serializers.PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save(author=request.user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("검증 오류", self.error())
            else:
                return Response("게시글 소유자가 아닙니다.", self.error())
        else:
            return Response("존재하지 않는 게시글입니다.", self.error())


class DeletePostView(APIView):
    def delete(self, request, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            post = get_object_or_404(post_models.Post, pk=pk)
            if post.author.pk == request.user.pk:
                post.delete()
                return Response("post is deleted", status=status.HTTP_200_OK)
            else:
                return Response("게시글 소유자가 아닙니다.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("post is not deleted", status=status.HTTP_400_BAD_REQUEST)


class PostListView(APIView):

    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        posts = (
            post_models.Post.objects.all()
            .select_related("author")
            .prefetch_related("tags", "like_set")
        )
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)


class CreatePostView(APIView):
    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        print(f"ss:{serializer}")
        print(f"user:{request.user}")

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
