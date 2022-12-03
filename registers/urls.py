from django.urls import path

from . views import (
    RegisterListView,
    RegisterCreateView,
    RegisterUpdateView,
    RegisterDetailView,
    RegisterDeleteView,
    pdffile,
)




urlpatterns = [
    path("list", RegisterListView.as_view(), name="register-list"),
    path("<int:pk>/", RegisterDetailView.as_view(), name="register-detail"),
    path("create/", RegisterCreateView.as_view(), name="register-create"),
    path("<int:pk>/update/", RegisterUpdateView.as_view(), name="register-update"),
    path("delete/<int:pk>/", RegisterDeleteView.as_view(), name="register-delete"),
    path("pdf/", pdffile, name="register-pdf"),

]

