from django.db import models
from django.urls import reverse
from django.utils import timezone
from registers.models import Register



class WaterInvoice(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    flow_consumed = models.FloatField()
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)


    class meta:
        ordering = ["name" "flow_consumed" "amount"]

    def __str__(self):
        return f"{self.name} - {self.flow_consumed} - {self.amount}"

    def get_absolute_url(self):
        return reverse("water-detail", kwargs={"pk": self.pk})





class ElectricityInvoice(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    kwatt_consumed = models.FloatField()
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)


    class meta:
        ordering = ["name" "kwatt_consumed" "amount"]

    def __str__(self):
        return f"{self.name} - {self.kwatt_consumed} - {self.amount}"

    def get_absolute_url(self):
        return reverse("electricity-detail", kwargs={"pk": self.pk})