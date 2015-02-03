import rest_framework_gis.filters
from rest_framework_gis.filterset import GeoFilterSet
from model import Site


class SiteFilter(GeoFilterSet):
    slug = filters.CharFilter(name='slug', lookup_type='istartswith')
    contains_geom = filters.GeometryFilter(name='geom', lookup_type='contains')

    class Meta:
        model = Site


