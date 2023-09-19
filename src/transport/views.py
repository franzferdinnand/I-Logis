from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from transport.models import Transport


class TransportListView(LoginRequiredMixin, ListView):
    template_name = "transport/transport_list.html"
    model = Transport
    context_object_name = "transport"

