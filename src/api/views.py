from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from api.serializers import (CargoSerializer, TransportSerializer,
                             UserSerializer)
from cargo.models import Cargo
from transport.models import Transport


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CargoListView(ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoDetailView(RetrieveAPIView):
    serializer_class = CargoSerializer

    def get_object(self):
        return Cargo.objects.get(pk=self.kwargs.get("pk"))


class TransportListView(ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportDetailView(RetrieveAPIView):
    serializer_class = TransportSerializer

    def get_object(self):
        return Transport.objects.get(pk=self.kwargs.get("pk"))


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
