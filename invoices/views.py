from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets


from .models import WaterInvoice, ElectricityInvoice


class WaterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = WaterInvoice
    fields = "__all__"
    success_message = "New water receipt create successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(WaterCreateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        return form


class WaterUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = WaterInvoice
    fields = "__all__"
    success_message = "Invoice updated successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(WaterUpdateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        return form


class WaterDetailView(LoginRequiredMixin, DetailView):
    model = WaterInvoice
    template_name = "invoices/waterinvoice_detail.html"

    def get_context_data(self, **kwargs):
        context = super(WaterDetailView, self).get_context_data(**kwargs)
        return context


###############################



class ElectricityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ElectricityInvoice
    fields = "__all__"
    success_message = "New electricity receipt create successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(ElectricityCreateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        return form


class ElectricityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ElectricityInvoice
    fields = "__all__"
    success_message = "invoice updated successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(ElectricityUpdateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        return form


class ElectricityDetailView(LoginRequiredMixin, DetailView):
    model = ElectricityInvoice
    template_name = "invoices/electricityinvoice_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ElectricityDetailView, self).get_context_data(**kwargs)
        return context
