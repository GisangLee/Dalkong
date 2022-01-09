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
        logged_in_user = request.user

        if pk is not None:
            user = get_object_or_404(user_models.User, pk=pk)

            print(f"현재 로그인 중인 유저 : {logged_in_user.username}")
            print(f"삭제하고자 하는 유저 : {user.username}")

            if logged_in_user.pk != user.pk:
                return Response("권한이 없습니다.", status=status.HTTP_400_BAD_REQUEST)

            else:
                user.delete()
                print(f"유저 계성 삭제 완료")
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

            if request.user.pk == user.pk:
                serializer = serializers.UpdateProfileSerializer(
                    user, data=request.data
                )

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)

                else:
                    return Response("invalid response", self.error())

            else:
                return Response("권한이 없습니다.", status=status.HTTP_400_BAD_REQUEST)

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
        to_follow_username = request.data["username"]
        current_user = request.user

        print(f"내가 팔로우 하고자 하는 유저이름 : {to_follow_username}")
        print(f"현재 로그인 유저 : {current_user.username}")

        to_follow_user = get_object_or_404(
            user_models.User, username=to_follow_username, is_active=True
        )

        # 내 입장 : 내가 팔로우하는 사람들 리스트에 추가
        current_user.following_set.add(to_follow_user)

        # 상대방 입장 : 나를 팔로잉 하는 사람들 리스트에 추가
        to_follow_user.follower_set.add(current_user)

        return Response(status.HTTP_204_NO_CONTENT)


class UserUnfollow(APIView):
    def post(self, request):
        to_unfollow_username = request.data["username"]
        current_user = request.user

        print(f"내가 언팔 하고싶은 유저이름 : {to_unfollow_username}")
        print(f"현재 로그인 유저 이름: {current_user.username}")

        follow_user = get_object_or_404(
            user_models.User, username=to_unfollow_username, is_active=True
        )

        # 내 입장: 내가 팔로우하는 사람들 리스트에서 제거
        current_user.following_set.remove(follow_user)

        # 상대방 입장: 나를 팔로잉하는 사람들 리스트에서 제거
        follow_user.follower_set.remove(current_user)

        return Response(status.HTTP_204_NO_CONTENT)
