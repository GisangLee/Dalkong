from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)
from posts import views as post_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("api-auth/", include("rest_framework.urls")),
    path("token/auth/", obtain_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/auth/", obtain_jwt_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
