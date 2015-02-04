Geospatial API for Site and Houshold optimization
==================================================================================================

Technologies used:
==================================================================================================
   * Django 1.7.3
   * Django Rest Framework 2.4.4
   * Celery
   * Postgis 
   * Postgres

==================================================================================================


==================================================================================================
Essential third party applications
==================================================================================================
   * Django Rest Framework GIS - 
     - https://github.com/djangonauts/django-rest-framework-gis
   * Celery
     - http://www.celeryproject.org/
   * Django Rest Framework
     - http://www.django-rest-framework.org/
   * Postgis
     - http://postgis.net/

==================================================================================================

==================================================================================================
Configuration and Databases
==================================================================================================
   The geo project is configured to run on postgres 9.3.5 using postgis, hstore, postgis_topology.
   Please see the geo/local_settings.py (DATABASES section) for the exact configuration
   Plsease refer to Postgis exvention for more info.
==================================================================================================

==================================================================================================
Models
==================================================================================================
We use django.contrib.gis.db for geospatial model types and Django Rest Framework GIS
for serializing those types
django-hstore is used for HStoreField  http://djangonauts.github.io/django-hstore/
The serialization is provided by Django Rest Framework GIS

==================================================================================================
Front-end technologies
==================================================================================================
   * Jinja2 - http://niwibe.github.io/django-jinja/
   * AngualarJS - https://angularjs.org/
   * Django Angular app - https://thinkster.io/django-angularjs-tutorial/

==================================================================================================
The demo data 
==================================================================================================
The demo data used in Django Rest Framework endpoints and a sample parser 
are available at excel directory. This data is currently displayed through the endpoints listed
below.

==================================================================================================
Algorithms for graph traversal and vertex counting
==================================================================================================
Please refer to the Algorithm.pdf document in the docs directory. Some basic logic for Kruskal
and A* provided in graph/graph.py and graph/kruskal.py. The pseudocode is included.



==================================================================================================
View Live Endpoint output
==================================================================================================
   * http://geo.zrealtycorp.com/households  
      - for households
   * http://geo.zrealtycorp.com/roadsegments
      - for road segments
   * http://geo.zrealtycorp.com/sites
      - for sites
   * http://geo.zrealtycorp.com/serviceareas
      - for service areas
   * http://geo.zrealtycorp.com/results
      - for computational results


==================================================================================================
Documentation
==================================================================================================
  Browse docs directory for more info

==================================================================================================
The installation contains minimal Django setup
needed to demonstrate Django Rest Framework API
access

=================================================================================================
Postgis Requirements
================================================================================================

To be able to use Postgis geospatial extensions for Postgres, please make sure 
the following third party software is installed on your Linux and is compliant 
with the Fedora/Debian versions:

  * GDAL   - http://download.osgeo.org/gdal/
  * GEOS   - http://download.osgeo.org/geos/
  * PROJ   - http://trac.osgeo.org/proj/
  * SFCGAL - http://oslandia.github.io/SFCGAL/

==================================================================================================
Deployment Requirements
==================================================================================================
This demo version of geo project is deployed on nginx server 1.7.7 using uwsgi
You might wish to customize the deployment script or use fabric deployment manager.
If used with a cloud, plsease refer to your cloud provider specs for using nginx.

----------------------------
Sample uwsgi command:
----------------------------
kill -9 $(pidof uwsgi)

cd /geo/geo

uwsgi --socket :8009 --module geo.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:9292 --daemonize=/var/www/vhosts/geo.zrealtycorp.com/logs/uwsg.log


This will run master process on port 8009 and span 4 slaves. The logs will be stored in uwsgi.log

 
