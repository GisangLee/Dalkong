from django.db import models
from accounts import models as user_models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampModel):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = "태그"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Post(TimeStampModel):
    author = models.ForeignKey(
        user_models.User, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=20)
    desc = models.TextField()
    # 하나의 게시글은 여러 태그, 하나의 태그는 여러 게시글
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)

    # 하나의 게시글은 여러 좋아요가 달린다.

    def __str__(self):
        return self.title


class Photo(TimeStampModel):
    file = models.ImageField(upload_to="posts/%Y/%m/%d")
    caption = models.TextField()
    room = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
