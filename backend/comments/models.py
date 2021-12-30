from django.db import models
from accounts import models as user_models
from posts import models as post_models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(TimeStampModel):
    user = models.ForeignKey(
        user_models.User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="작성자",
    )
    post = models.ForeignKey(
        post_models.Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="게시글",
    )
    desc = models.CharField(max_length=255, verbose_name="댓글 내용")

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"
