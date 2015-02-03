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


class ServiceArea(models.Model):
    custom_attributes = HStoreField(null=True)
    geo_attributes = HStoreField(null=True)
    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    shape = models.MultiPolygonField(null=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'service area'
        verbose_name_plural = 'service areas'


class RoadSegment(models.Model):
    service_area_id = models.ForeignKey(ServiceArea)
    node_from_id = models.IntegerField(default=0)
    node_to_id = models.IntegerField(default=0)
    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    length = models.IntegerField(default=0)
    shape = models.MultiLineStringField(null=True)
    objects = models.GeoManager()

    class Meta:
        verbose_name = 'road segment'
        verbose_name_plural = 'road segments'



class Site(models.Model):
    service_area_id = models.ForeignKey(ServiceArea)
    road_segment_id = models.ForeignKey(RoadSegment,null=True)
    site_type = models.IntegerField(default=0)     
    deployment_date = models.DateField(null=True)
    coordinates = models.PointField()
    objects = models.GeoManager()
    road_segment_start_distance = models.IntegerField(default=0)
    road_segment_end_distance = models.IntegerField(default=0)
    custom_attributes = HStoreField(null=True)
        
    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'sites'


class HouseHold(models.Model):
    service_area_id = models.ForeignKey(ServiceArea)
    road_segment_id = models.ForeignKey(RoadSegment,null=True)
    address_street = models.CharField(max_length=100,null=True)
    address_city = models.CharField(max_length=100,null=True)
    address_state = models.CharField(max_length=30,null=True)
    address_zip = models.CharField(max_length=10,null=True)
    coordinates = models.PointField()
    objects = models.GeoManager()
    road_segment_start_distance = models.IntegerField(default=0)
    road_segment_end_distance = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'household'
        verbose_name_plural = 'households'


"""
    ServiceArea
"""
class ServiceAreaList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        serviceareas = ServiceArea.objects.all()
        serializer = PropertySerializer(serviceareas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

