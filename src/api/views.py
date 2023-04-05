from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveUpdateAPIView)

from api.serializers import CargoSerializer, TransportSerializer
from cargo.models import Cargo
from transport.models import Transport


class CargoListView(ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class TransportListView(ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportCreateView(CreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportUpdateView(RetrieveUpdateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    http_method_names = ["patch", "put"]
    lookup_field = "id"


class TransportDeleteView(DestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    http_method_names = ["delete"]
    lookup_field = "id"


class CargoCreateView(CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoUpdateView(RetrieveUpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    http_method_names = ["patch", "put"]
    lookup_field = "id"


class CargoDeleteView(DestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    http_method_names = ["delete"]
    lookup_field = "id"
