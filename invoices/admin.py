from django.contrib import admin
from .models import WaterInvoice, ElectricityInvoice




admin.site.register(WaterInvoice)
admin.site.register(ElectricityInvoice)

