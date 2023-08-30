from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class UserRegistrationView(CreateView):
    pass
    template_name = ...
    form_class = ...
    success_url = ... # reverse_lazy


class UserLoginView(LoginView):
    ...


class UserLogoutView(LogoutView):
    ...

