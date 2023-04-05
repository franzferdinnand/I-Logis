from rest_framework import serializers

from account.models import UserAccount
from cargo.models import Cargo
from transport.models import Transport


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["id", "first_name", "last_name", "email", "user_type"]


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ["id", "cargo_type", "weight_kg", "destination_from", "destination_to", "owner"]


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ["id", "car_name", "car_model", "max_weight", "owner"]
