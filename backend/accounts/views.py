from django.shortcuts import render
from accounts import models, serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import models as user_models


class UpdateProfileView(APIView):
    def error(self):
        return status.HTTP_400_BAD_REQUEST

    def put(self, request, **kwargs):
        if kwargs.get("pk") is not None:
            pk = kwargs.get("pk")
            user = user_models.User.objects.get(pk=pk)
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
        model = user_models.User
        serializer = serializers.SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
