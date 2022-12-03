from django.urls import path

from .views import (
    WaterCreateView,
    WaterDetailView,
    WaterUpdateView,
    ElectricityCreateView,
    ElectricityDetailView,
    ElectricityUpdateView,
)



urlpatterns = [
    path("water/create", WaterCreateView.as_view(), name="water-create"),
    path("water/<int:pk>", WaterDetailView.as_view(), name="water-detail"),
    path("water/<int:pk>/update", WaterUpdateView.as_view(), name="water-update"),
    path("electricity/create", ElectricityCreateView.as_view(), name="electricity-create"),
    path("electricity/<int:pk>", ElectricityDetailView.as_view(), name="electricity-detail"),
    path("electricity/<int:pk>/update", ElectricityUpdateView.as_view(), name="electricity-update"),
]