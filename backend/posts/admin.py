from django.contrib import admin
from . import models as post_models

# Register your models here.


class TagInlie(admin.TabularInline):
    model = post_models.Photo


@admin.register(post_models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "author",
        "title",
        "desc",
    )

    list_filter = ("tags",)

    inlines = (TagInlie,)

    fieldsets = (
        (
            "게시글 기본 정보",
            {
                "fields": (
                    "autor",
                    "title",
                    "desc",
                ),
            },
        ),
        (
            "태그 정보",
            {
                "fields": ("tags",),
            },
        ),
    )

    filter_horizontal = ("tags",)
