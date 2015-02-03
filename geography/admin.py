from django.contrib import admin
from models import ServiceArea,Site,RoadSegment,HouseHold
# Register your models here.
"""
  Register the models with Dajngo Admin
"""

class ServiceAreaAdmin(admin.ModelAdmin):
    fiels = ('custom_attributes','geo_attributes','shape',)

class SiteAdmin(admin.ModelAdmin):
    fiels = ('service_area','site_segment','site_type','deployment_date','coordinates')

class RoadSegmenteAdmin(admin.ModelAdmin):
    fiels = ('service_area','node_from','node_to','shape','length',)

class HouseHoldAdmin(admin.ModelAdmin):
    fiels = ('service_area','road_segment','address_street',
             'address_city','address_state','address_zip','coordinates',
             'road_segment_start_distance','road_segment_end_distance')


admin.site.register(ServiceArea)
admin.site.register(RoadSegment)
admin.site.register(Site)
admin.site.register(HouseHold)

