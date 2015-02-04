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
from serializers import HouseholdResultSerializer
from models import HouseholdResult

"""
Household Result ViewSet
"""
class HouseholdResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view the result.
    """
    queryset = HouseholdResult.objects.all()
    serializer_class = HouseholdResultSerializer

