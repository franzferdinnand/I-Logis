from account.models import UserAccount
from cargo.models import Cargo
from transport.models import Transport


def sample_cargo(user, **kwargs):
    default = {
        "cargo_type": "bullets",
        "weight_kg": "3000",
        "destination_from": "Warsaw",
        "destination_to": "Kyiv",
        "owner": user,
    }
    default.update(kwargs)
    return Cargo.objects.create(**default)


def sample_transport(user, **kwargs):
    default = {
        "car_name": "bullets",
        "car_model": "3000",
        "max_weight": "Warsaw",
        "owner": user,
    }
    default.update(kwargs)
    return Transport.objects.create(**default)


def sample_user_account(**kwargs):
    default = {
        "phone_number": "570320320",
        "first_name": "serhii",
        "last_name": "turchyn",
        "email": "admin@admin.com",
        "user_type": "2",
    }

    default.update(kwargs)
    return UserAccount.objects.create(**default)
