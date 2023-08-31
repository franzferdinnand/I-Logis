from django.contrib import admin
from django.urls import include, path


app_name = "core"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("core.urls")),
]
