from django.db import models

"""
  User Input geo data - we use this as a form model
"""
class GeoData(models.Model):
    threshold = models.CharField(max_length=100)
    site = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'geo data'
        verbose_name_plural = 'geo data'

"""
  Canvas - we use this model to display results.
"""
class Canvas(models.Model):
    class Meta:
        verbose_name = 'canvas'
        verbose_name_plural = 'canvas'


    
