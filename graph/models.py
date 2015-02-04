from django.db import models

"""
  Result model - the number of households for given input
"""
class HouseholdResult(models.Model):
    result = models.CharField(max_length=400,blank=True, null=True)


