from django.urls import path

from api.views import (CargoCreateView, CargoDeleteView, CargoListView,
                       CargoUpdateView, TransportCreateView,
                       TransportDeleteView, TransportListView,
                       TransportUpdateView)

app_name = "api"

urlpatterns = [
    path("cargos/", CargoListView.as_view(), name="cargos"),
    path("transports/", TransportListView.as_view(), name="transports"),
    path("create-transport/", TransportCreateView.as_view(), name="create_transport"),
    path("update-transport/<int:id>/", TransportUpdateView.as_view(), name="update_transport"),
    path("delete-transport/<int:id>/", TransportDeleteView.as_view(), name="delete_transport"),
    path("create-cargo/", CargoCreateView.as_view(), name="create_cargo"),
    path("update-cargo/<int:id>/", CargoUpdateView.as_view(), name="update_cargo"),
    path("delete-cargo/<int:id>/", CargoDeleteView.as_view(), name="delete_cargo"),
]
