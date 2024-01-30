from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from cargo.models import Cargo


class CargoListView(LoginRequiredMixin, ListView):
    template_name = "cargo/cargo_list.html"
    model = Cargo
    context_object_name = "cargo"


class CargoCreateView(LoginRequiredMixin, CreateView):
    template_name = "cargo/create_cargo.html"
    model = Cargo
    fields = "__all__"
    success_url = reverse_lazy("cargo:cargos")


class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo



