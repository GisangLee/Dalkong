from . import models as user_models
from rest_framework import serializers


class UserSerializer:
    class Meta:
        model = user_models.User
        fields = "__all__"


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ["pk", "bio", "avatar"]


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print(f"data : {validated_data}")
        req_password = validated_data.pop("password")
        user = user_models.User.objects.create(**validated_data)
        user.set_password(req_password)
        user.save()
        return user

    class Meta:
        model = user_models.User
        fields = ["pk", "username", "email", "password", "bio", "gender", "birthdate"]
