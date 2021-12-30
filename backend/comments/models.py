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
        user_models.User, on_delete=models.CASCADE, related_name="comments"
    )
    room = models.ForeignKey(
        post_models.Post, on_delete=models.CASCADE, related_name="comments"
    )
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.desc
