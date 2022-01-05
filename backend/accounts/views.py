from django.shortcuts import render, get_object_or_404
from accounts import models, serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import models as user_models


class DeleteUserView(APIView):
    def delete(self, request, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            user = get_object_or_404(user_models.User, pk=pk)
            print(f"username : {user.username}")
            user.delete()
            return Response("user deleted", status=status.HTTP_200_OK)
        else:
            return Response("user not deleted", status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(APIView):
    def error(self):
        return status.HTTP_400_BAD_REQUEST

    def put(self, request, **kwargs):
        if kwargs.get("pk") is not None:
            pk = kwargs.get("pk")
            user = get_object_or_404(user_models.User, pk=pk)
            print(f" username: {user.username}")
            serializer = serializers.UpdateProfileSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid response", self.error())
        else:
            return Response("invalid response", self.error())


class SignupView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, format=None):
        serializer = serializers.SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class UserFollow(APIView):
    def post(self, request):
        username = request.data["username"]
        print(f"username : {username}")
        follow_user = get_object_or_404(
            user_models.User, username=username, is_active=True
        )
        request.user.following_set.add(follow_user)
        follow_user.follower_set.add(request.user)
        return Response(status.HTTP_204_NO_CONTENT)


class UserUnfollow(APIView):
    def post(self, request):
        username = request.data["username"]
        print(f"username : {username}")
        follow_user = get_object_or_404(
            user_models.User, username=username, is_active=True
        )
        request.user.following_set.remove(follow_user)
        follow_user.follower_set.remove(request.user)
        return Response(status.HTTP_204_NO_CONTENT)
