from django.contrib import admin
from django.urls import include, path


app_name = "core"


urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/", include("api.urls")),
    path(r"", include("core.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),

]
