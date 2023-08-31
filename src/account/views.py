from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        # send_registration_email(request=self.request, user_instance=self.object)

        return super().form_valid(form)


class UserLoginView(LoginView):
    next_page = reverse_lazy('core:index')


class UserLogoutView(LogoutView):
    template_name = "index.html"
