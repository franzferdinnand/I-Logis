from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CargoCreateView, CargoDeleteView, CargoDetailView,
                       CargoListView, CargoUpdateView, TransportCreateView,
                       TransportDeleteView, TransportDetailView,
                       TransportListView, TransportUpdateView, UserViewSet)
from django.conf import settings

from config.settings import dev
from core.views import UserProfileView

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="I-Logis API",
        default_version="v1.0",
        description="API for using of cargo or drivers info",
        term_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger_docs"),
    path("cargos/", CargoListView.as_view(), name="cargos"),
    path("cargo-detail/<int:pk>/", CargoDetailView.as_view(), name="cargo-detail"),
    path("transports/", TransportListView.as_view(), name="transports"),
    path("transport-detail/<int:id>/", TransportDetailView.as_view(), name="transport-detail"),
    path("create-transport/", TransportCreateView.as_view(), name="create_transport"),
    path("update-transport/<int:id>/", TransportUpdateView.as_view(), name="update_transport"),
    path("delete-transport/<int:id>/", TransportDeleteView.as_view(), name="delete_transport"),
    path("create-cargo/", CargoCreateView.as_view(), name="create_cargo"),
    path("update-cargo/<int:id>/", CargoUpdateView.as_view(), name="update_cargo"),
    path("delete-cargo/<int:id>/", CargoDeleteView.as_view(), name="delete_cargo"),
    path("api_profile/<int:pk>", UserProfileView.as_view(), name="api_profile"),
] + static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

