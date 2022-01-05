from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("update/<int:pk>/", views.UpdateProfileView.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteUserView.as_view(), name="delete"),
    path("follow/", views.UserFollow.as_view(), name="follow"),
    path("unfollow/", views.UserUnfollow.as_view(), name="unfollow"),
]
