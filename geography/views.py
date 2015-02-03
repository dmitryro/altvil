from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from serializers import ServiceAreaSerializer
from serializers import RoadSegmentSerializer
from serializers import HouseHoldSerializer
from serializers import SiteSerializer
from models import ServiceArea, RoadSegment, HouseHold, Site

"""
Service Area ViewSet
"""
class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows service areas to be viewed or edited.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


"""
Road Segment ViewSet
"""
class RoadSegmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows road segments to be viewed or edited.
    """
    queryset = RoadSegment.objects.all()
    serializer_class = RoadSegmentSerializer


"""
HouseHold ViewSet
"""
class HouseHoldViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows households to be viewed or edited.
    """
    queryset = HouseHold.objects.all()
    serializer_class = HouseHoldSerializer


"""
Site ViewSet
"""
class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

