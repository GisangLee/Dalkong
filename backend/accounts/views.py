from django.shortcuts import render
from accounts import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from . import models as user_models


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
