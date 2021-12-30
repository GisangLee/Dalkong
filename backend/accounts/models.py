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

    LOGIN_KAKAO = "카카오"
    LOGIN_EMAIL = "이메일"
    LOGIN_CHOICE = ((LOGIN_KAKAO, "카카오"), (LOGIN_EMAIL, "이메일"))

    follower_set = models.ManyToManyField("self", blank=True, verbose_name="나를 팔로우")
    following_set = models.ManyToManyField("self", blank=True, verbose_name="내가 팔로우")
    email = models.EmailField(max_length=200, verbose_name="이메일")
    bio = models.CharField(max_length=255, blank=True, verbose_name="소개")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=2, blank=True, verbose_name="성별"
    )
    avatar = models.ImageField(
        upload_to="user_profile/%Y/%m/%d", blank=True, verbose_name="프로필 사진"
    )
    birthdate = models.DateField(blank=True, null=True, verbose_name="생일")
    email_verified = models.BooleanField(default=False, verbose_name="이메일 인증 여부")
    email_secret = models.CharField(
        max_length=120, default="", blank=True, verbose_name="이메일 인증 키"
    )
    login_method = models.CharField(
        choices=LOGIN_CHOICE, max_length=3, default=LOGIN_EMAIL, verbose_name="로그인 방법"
    )

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
