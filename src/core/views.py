from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView

from account.models import UserAccount


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile/user_profile.html'
    model = UserAccount
    queryset = UserAccount.objects.all()
