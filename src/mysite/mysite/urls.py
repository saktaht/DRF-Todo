from django.contrib import admin
from django.urls import path, include

from app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    #トークン認証
    path("api-auth/", include("dj_rest_auth.urls")),
    path("app/", include("app.urls")),
]
