from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView


class IndexView(TemplateView):
    template_name = "index.html"
    http_method_names = ["get"]


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = "profile/user_profile.html"
    model = get_user_model()
    queryset = get_user_model().objects.all()
