from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import viewsets, routers
import rules_light
import smart_selects
from geography import views
from graph.views import HouseholdResultViewSet

router = routers.DefaultRouter()
router.register(r'serviceareas', views.ServiceAreaViewSet)
router.register(r'roadsegments', views.RoadSegmentViewSet)
router.register(r'households', views.HouseHoldViewSet)
router.register(r'sites', views.SiteViewSet)
router.register(r'results', HouseholdResultViewSet)
admin.autodiscover()




urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/geography/',include(admin.site.urls)),
    url(r'^admin/geography/site/$',include(admin.site.urls)),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/geography/servicearea/add/$',include(admin.site.urls)),
    url(r'^home/$', ('gui.views.get_canvas')),
    url(r'^canvas/$', ('gui.views.get_canvas')),
    url(r'^', include(router.urls)),
)
