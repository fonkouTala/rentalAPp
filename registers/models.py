from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone




class Register(models.Model):
    RENT_TYPE = [("chambre", "chambre"), ("studio", "studio"), ("appartement", "appartement")]

    full_name = models.CharField("Enter Full Name",  max_length=250)
    cni_no = models.IntegerField(unique=True)
    rent_type = models.CharField(max_length=15, choices=RENT_TYPE)
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    phone = models.CharField("Phone number", validators=[mobile_num_regex], max_length=13, blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField("Street address", max_length=150)
    date = models.DateField("Start date", default=timezone.now)
    amount = models.IntegerField("Amount paid")


    class meta:
        ordering = ["full_name" "rent_type" "email"]


    def __str__(self):
        return f"{self.full_name} - {self.rent_type} - {self.email}"


    def get_absolute_url(self):
        return reverse("register-detail", kwargs={"pk": self.pk})

    

    