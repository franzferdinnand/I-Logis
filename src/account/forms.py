from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["phone_number", "email", "first_name", "last_name", "password1", "password2"]

        def clean(self):
            _cleaned_data = super().clean()

            if not bool(_cleaned_data["email"]) and not not bool(_cleaned_data["phone_number"]):
                raise ValidationError("Insert email or phone number. At least one of them, please")

            elif not bool(_cleaned_data["email"]):
                if get_user_model().objects.filter(phone_number=_cleaned_data["phone_number"]).exists():
                    raise ValidationError("User with this phone number already exists!!!")

            elif not bool(_cleaned_data["phone_number"]):
                if get_user_model().objects.filter(phone_number=_cleaned_data["email"]).exists():
                    raise ValidationError("User with this email already exists!!!")

            return _cleaned_data
