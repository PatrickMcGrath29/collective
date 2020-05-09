from django_countries.fields import CountryField
from django.db import models

class Foundation(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    headquarters_address = models.CharField(max_length=50)
    country = CountryField()

    def __str__(self):
        return self.name

