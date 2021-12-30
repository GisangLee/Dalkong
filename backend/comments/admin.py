from django.contrib import admin
from . import models as comment_models

# Register your models here.


@admin.register(comment_models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        "user",
        "post",
        "desc",
    )

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            "title": "댓글 목록",
        }
        return super().changelist_view(request, extra_context)

    fieldsets = (
        (
            "댓글 정보",
            {
                "fields": ("desc", "user", "post"),
            },
        ),
    )
