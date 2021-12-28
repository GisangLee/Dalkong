from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    GENDER_MALE = "남자"
    GENDER_FEMALE = "여자"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
    )

    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)
    email = models.EmailField(max_length=200)
    bio = models.CharField(max_length=255, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2, blank=True)
    avatar = models.ImageField(upload_to="user_profile/%Y/%m/%d", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)
