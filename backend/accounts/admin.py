from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as user_models

# Register your models here.


@admin.register(user_models.User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "bio",
        "gender",
        "avatar",
        "birthdate",
        "email_verified",
    )

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            "title": "사용자 목록",
        }
        return super().changelist_view(request, extra_context)

    fieldsets = (
        (
            "유저 기본 정보",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                ),
            },
        ),
    ) + UserAdmin.fieldsets
