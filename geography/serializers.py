from rest_framework_gis.serializers import GeoFeatureModelSerializer
from models import ServiceArea,RoadSegment,Site,HouseHold


class ServiceAreaSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = ServiceArea
        geo_field = "shape"
        id_field = False
        fields = ('id', 'custom_attributes', 'geo_attributes', 'shape')


class RoadSegmentSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = RoadSegment
        geo_field = "shape"
        id_field = False
        fields = ('id', 'service_area_id','node_from_id','node_to_id', 'shape', 'length')

class SiteSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Site
        geo_field = "coordinates"
        id_field = False
        fields = ('id', 'service_area_id','coordinates','custom_attributes','deployment_date',
                  'road_segment_end_distance','road_segment_id','road_segment_start_distance','site_type')
   

class HouseHoldSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = HouseHold
        geo_field = "coordinates"
        id_field = False
        fields = ('id','address_street','address_city','address_state',
                  'address_zip','coordinates','road_segment_start_distance',
                  'road_segment_end_distance','road_segment_id','service_area_id')

