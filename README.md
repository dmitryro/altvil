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
Models
==================================================================================================
We use django.contrib.gis.db for geospatial model types and Django Rest Framework GIS
for serializing those types


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
are available at excel directory




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

