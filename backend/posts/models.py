from django.db import models
from accounts import models as user_models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampModel):
    name = models.CharField(max_length=10, verbose_name="태그명")

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Post(TimeStampModel):
    author = models.ForeignKey(
        user_models.User,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    title = models.CharField(max_length=20, verbose_name="글 제목")
    desc = models.TextField(verbose_name="글 내용")
    # 하나의 게시글은 여러 태그, 하나의 태그는 여러 게시글
    tags = models.ManyToManyField(
        "Tag", related_name="posts", blank=True, verbose_name="태그"
    )

    # 하나의 게시글은 여러 좋아요가 달린다.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"


class Photo(TimeStampModel):
    file = models.ImageField(upload_to="posts/%Y/%m/%d", verbose_name="파일")
    caption = models.TextField(verbose_name="설명", blank=True)
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, verbose_name="해당 게시글", related_name="photos"
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "게시글 사진"
        verbose_name_plural = "게시글 사진"
