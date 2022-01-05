from django.contrib import admin
from . import models as post_models

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = post_models.Photo


@admin.register(post_models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "pk",
        "author",
        "title",
        "desc",
    )

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            "title": "게시글 목록",
        }
        return super().changelist_view(request, extra_context)

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "게시글 기본 정보",
            {
                "fields": (
                    "author",
                    "title",
                    "desc",
                ),
            },
        ),
        (
            "태그 정보",
            {
                "fields": ("tags", "like_set"),
            },
        ),
    )

    filter_horizontal = ("tags", "like_set")
