from django.urls import include, path

from account.views import UserRegistrationView
from core.views import IndexView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
]