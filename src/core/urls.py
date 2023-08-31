from django.urls import include, path

from account.views import UserRegistrationView, UserLoginView, UserLogoutView
from core.views import IndexView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]