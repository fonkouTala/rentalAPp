from django.db import models
from django.utils import timezone
from django.urls import reverse
from registers.models import Register



class Issue(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    picture = models.FileField(upload_to="issues/pictures")
    description = models.TextField()

    class meta:
        ordering = ["name" "date" "picture"]

    def __str__(self):
        return f"{self.name} - {self.date} - {self.description}"

    def get_absolute_url(self):
        return reverse("issue-detail", kwargs={"pk": self.pk})