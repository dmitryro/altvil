from django.contrib.gis.db import models
from django.forms import Textarea
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from django_hstore.fields import HStoreField
from django.http import HttpResponse
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey
from djangular.views.mixins import JSONResponseMixin, allow_remote_invocation

"""
  Service Area Model
"""
class ServiceArea(models.Model):
    custom_attributes = HStoreField(null=True) # HStoreField provides flexible geo storage
    geo_attributes = HStoreField(null=True) # HStoreField
    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    shape = models.MultiPolygonField(null=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'service area'
        verbose_name_plural = 'service areas'

"""
  Road Segment Model
"""
class RoadSegment(models.Model):
    service_area_id = models.ForeignKey(ServiceArea) 
    node_from_id = models.IntegerField(default=0)
    node_to_id = models.IntegerField(default=0)
    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    length = models.IntegerField(default=0)
    shape = models.MultiLineStringField(null=True)
    objects = models.GeoManager()  # GeoManageer is used to mange polygonal fields

    class Meta:
        verbose_name = 'road segment'
        verbose_name_plural = 'road segments'

"""
  Site Model
"""
class Site(models.Model):
    service_area_id = models.ForeignKey(ServiceArea)
    road_segment_id = models.ForeignKey(RoadSegment,null=True)
    site_type = models.IntegerField(default=0)     
    deployment_date = models.DateField(null=True)
    coordinates = models.PointField()
    objects = models.GeoManager() # GeoManageer is used to mange polygonal fields
    road_segment_start_distance = models.IntegerField(default=0)
    road_segment_end_distance = models.IntegerField(default=0)
    custom_attributes = HStoreField(null=True)
        
    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'sites'

"""
  Household Model
"""
class HouseHold(models.Model):
    service_area_id = models.ForeignKey(ServiceArea)
    road_segment_id = models.ForeignKey(RoadSegment,null=True)
    address_street = models.CharField(max_length=100,null=True)
    address_city = models.CharField(max_length=100,null=True)
    address_state = models.CharField(max_length=30,null=True)
    address_zip = models.CharField(max_length=10,null=True)
    coordinates = models.PointField() # Point format provided by django
    objects = models.GeoManager()  # GeoManageer is used to mange polygonal fields
    road_segment_start_distance = models.IntegerField(default=0)
    road_segment_end_distance = models.IntegerField(default=0)

    class Meta: # Build the class
        verbose_name = 'household'
        verbose_name_plural = 'households'



