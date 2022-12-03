from django.urls import path 

from .views import (
    StatementListView,
    StatementDetailView,
    StatementCreateView,
    StatementDeleteView,
    StatementUpdateView,
)

urlpatterns = [
    path("list/", StatementListView.as_view(), name="statement-list"),
    path("create/", StatementCreateView.as_view(), name="statement-create"),
    path("<int:pk>/", StatementDetailView.as_view(), name="statement-detail"),
    path("delete/<int:pk>/", StatementDeleteView.as_view(), name="statement-delete"),
    path("<int:pk>/update/", StatementUpdateView.as_view(), name="statement-update"),
]