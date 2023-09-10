from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from account.views import (ActivateUser, UserLoginView, UserLogoutView,
                           UserRegistrationView)
from core.views import IndexView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("activate/<str:uuid64>/<str:token>", ActivateUser.as_view(), name="activate_user"),
]
