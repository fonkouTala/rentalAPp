from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Issue


class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = "issues/issue_list.html"
    


class IssueCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Issue
    fields = "__all__"
    success_message = "New issue add successfully"

    def get_form(self):
        """add date picker format"""
        form = super(IssueCreateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["description"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class IssueUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Issue
    fields = "__all__"
    success_message = "issue successfully updated."

    def get_form(self):
        """add date and text picker in forms"""
        form = super(IssueUpdateView, self).get_form()
        form.fields["date"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["description"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        return context


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy("issue-list")



