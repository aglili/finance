from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    savings = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.username
