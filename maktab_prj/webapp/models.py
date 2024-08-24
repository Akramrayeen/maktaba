from django.db import models
from cities_light.models import Country, Region, City

class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

