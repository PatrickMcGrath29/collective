from django_countries.fields import CountryField
from django.db import models

class Foundation(models.Model):
    # TODO: Add user field
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    headquarters_address = models.CharField(max_length=50)
    country = CountryField()

    def __str__(self):
        return self.name

class ContentUpdate(models.Model):
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)

    def __str__(self):
        return '{} - {}'.format(self.foundation, self.title)
