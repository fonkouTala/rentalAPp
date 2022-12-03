from django.db import models
from django.urls import reverse
from django.utils import timezone

from registers.models import Register


class Statement(models.Model):
    name = models.ForeignKey(Register, verbose_name='Full name', on_delete=models.CASCADE)
    start_date = models.DateField("Start date", default=timezone.now)
    end_date = models.DateField("End date", default=timezone.now)
    balance = models.FloatField("Balance brought forward")
    final_balance = models.FloatField("Final balance")
    description = models.TextField("Description", blank=True)

    class meta:
        ordering = ["name" "start_date" "end_date"]


    def __str__(self):
        return f"{self.name}-{self.start_date}-{self.end_date}"


    def get_absolute_url(self):
        return reverse("statement-detail", kwargs={"pk": self.pk})


