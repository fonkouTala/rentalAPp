from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Statement

#some importations to use in reportlab which generate pdf file in django
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


class StatementListView(LoginRequiredMixin
, ListView):
    model = Statement
    template_name = "statements/statement_list.html"
    context = Statement.objects.all()


class StatementCreateView(LoginRequiredMixin
, SuccessMessageMixin, CreateView):
    model = Statement
    fields = "__all__"
    success_message = "New statement add successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(StatementCreateView, self).get_form()
        form.fields["start_date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["end_date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["description"].widget = widgets.Textarea(attrs={"rows": 2})
        return form

class StatementUpdateView(LoginRequiredMixin
, SuccessMessageMixin, UpdateView):
    model = Statement
    fields = "__all__"
    success_message = "statement updated successfully"

    def get_form(self):
        """add date picker in form"""
        form = super(StatementUpdateView, self).get_form()
        form.fields["start_date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["end_date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["description"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StatementDetailView(LoginRequiredMixin
, DetailView):
    model = Statement
    template_name = "statements/statement_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StatementDetailView, self).get_context_data(**kwargs)
        return context


class StatementDeleteView(LoginRequiredMixin
, DeleteView):
    model = Statement
    success_url = reverse_lazy("statement-list")



##for reportlab using
def pdf2(request):
    pass