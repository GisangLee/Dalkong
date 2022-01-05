from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("postlist/", views.PostListView.as_view(), name="postlist"),
    path("createpost/", views.CreatePostView.as_view(), name="create-post"),
    path("deletepost/<int:pk>/", views.DeletePostView.as_view(), name="delete-post"),
    path("updatepost/<int:pk>/", views.UpdatePostView.as_view(), name="update-post"),
]
