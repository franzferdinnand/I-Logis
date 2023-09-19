from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from config.settings import dev

app_name = "core"


urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/", include("api.urls")),
    path(r"", include("core.urls")),
    path(r"cargo/", include("cargo.urls")),
    path(r"transport/", include("transport.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),

] + static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
