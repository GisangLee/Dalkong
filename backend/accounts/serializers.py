from . import models as user_models


class UserSerializer:
    class Meta:
        model = user_models.User
        fields = "__all__"


class JwtLoginSerializer:
    pass


class SignupSerializer:
    pass
