from django.urls import path

from .views import (
    IssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueUpdateView,
    IssueDeleteView,


)


urlpatterns = [
    path("list/", IssueListView.as_view(), name="issue-list"),
    path("<int:pk>/", IssueDetailView.as_view(), name="issue-detail"),
    path("create/", IssueCreateView.as_view(), name="issue-create"),
    path("<int:pk>/uptade", IssueUpdateView.as_view(), name="issue-update"),
    path("<int:pk>/delete", IssueDeleteView.as_view(), name="issue-delete"),

]