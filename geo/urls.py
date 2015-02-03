from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import viewsets, routers
import rules_light
import smart_selects
from geography import views
#from gui.views import CanvasView

router = routers.DefaultRouter()
router.register(r'serviceareas', views.ServiceAreaViewSet)
router.register(r'roadsegments', views.RoadSegmentViewSet)
router.register(r'households', views.HouseHoldViewSet)
router.register(r'sites', views.SiteViewSet)
#router.register(r'cities/$', views.CityViewSet)
#router.register(r'oblasts', views.OblastViewSet)
#router.register(r'categories',views.CategoryViewSet)
#router.register(r'units',views.UnitViewSet)
#router.register(r'countries',views.CountryViewSet)
#router.register(r'federaldistricts',views.FederalDistrictViewSet)
#router.register(r'subjects',views.FederalSubjectViewSet)


rules_light.autodiscover()
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
    #url(r'^oblasts/$', views.OblastViewSet.as_view({
    #  'get': 'list'
    #}
    #)),
    #url(r'^categories/$', views.CategoryViewSet.as_view({
    #  'get': 'list'
    #}
    #)),
    url(r'^', include(router.urls)),

    #url(r'^cities/$', views.CityViewSet.as_view({
    #  'get': 'list'
    #}
    #)),
    #url(r'^cities/(?P<pk>[0-9]+)/$', views.city_detail),
)
