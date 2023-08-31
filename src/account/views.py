from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('config:index')


class UserLoginView(LoginView):
    ...


class UserLogoutView(LogoutView):
    ...

