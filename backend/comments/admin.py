from django.contrib import admin
from . import models as comment_models

# Register your models here.


@admin.register(comment_models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        "user",
        "room",
        "desc",
    )

    fieldsets = (
        (
            "댓글 정보",
            {
                "fields": ("desc", "user", "room"),
            },
        ),
    )
