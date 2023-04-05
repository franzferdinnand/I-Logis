from django.contrib import admin
from django.urls import include, path

from core.views import IndexView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", IndexView.as_view(), name="index"),
]
