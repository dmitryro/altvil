"""
Django settings for zrealty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=vya07wc_h+a^cmm!o#j**w(ipl(r$n(#k#b2)94(*9#iv1@('
SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Social Authentication Settings
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

# Application definition

# Possible values are Tokenizer (default), JaroWinkler and LevenshteinDistance.
# JaroWinkler and LevenshteinDistance require Levenshtein Module >= 0.10.1.
USER_AGENT_SEARCH_ALGORITHM = 'Tokenizer'

EASY_MAPS_CENTER = (-41.3, 32)

#SOUTH_MIGRATION_MODULES = {
#    'easy_thumbnails': 'easy_thumbnails.south_migrations',
#    'taggit': 'taggit.south_migrations',
#}

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    #contributed apps
   # 'modernizr',
    'admin_tools',
    'adminsortable',
  #  'ajax_select',
    'any_urlfield',
    'corsheaders',
    'djangular',
    'coffeescript',
    'bootstrap',
    'bootstrap_toolkit',
    'bootstrap_pagination',
    'uni_form',
    'django_actions',
    'django_extensions',
    'django_filters',
    'django_google_maps',
   # 'feedme',
   # 'feedreader',
    'admin_import',
    'geoposition',
    'gmapi',
    'i18n',
    'jinja2',
    'permission',
    'pygments',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_digestauth',
    'rest_framework_gis',
    'rest_framework_bulk',
    'rules_light',
    # Custom apps
    'geography',
    'graph',
    'gui',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'rules_light.middleware.Middleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = {
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_rules.backends.ObjectPermissionBackend',
)
   

ROOT_URLCONF = 'geo.urls'



# The name of a build profile to use for your project, relative to REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the built-in default build profile.
# Set to False to disable running the default profile (e.g. if only using it to build Standalone
# Modules)
REQUIRE_BUILD_PROFILE = None

# The name of the require.js script used by your project, relative to REQUIRE_BASE_URL.

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {}

# Whether to run django-require in debug mode.

# A tuple of files to exclude from the compilation result of r.js.
REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: auto, node or rhino.
# auto will autodetect the environment and make use of node if available and rhino if not.
# It can also be a path to a custom class that subclasses require.environments.Environment and defines some "args" function that returns a list with the command arguments to execute.
REQUIRE_ENVIRONMENT = "auto"
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geodjango',
         'USER': 'geo',
     }
}

DEFAULT_AUTHENTICATION = (
   # 'rest_framework.authentication.BasicAuthentication',
   # 'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.OAuth2Authentication',
)

GRAPPELLI_ADMIN_TITLE = 'Geo Location'

GRAPPELLI_INDEX_DASHBOARD = {
   'django.contrib.admin.site': 'artwell.dashboard.CustomIndexDashboard',
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
#       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.OAuth2Authentication',
     ),
    'DEFAULT_PARSER_CLASSES': (

        'rest_framework.parsers.YAMLParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'PAGINATE_BY': 1000, 

    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
 
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/vhosts/geo.zrealtycorp.com/geo/static/'
MEDIA_ROOT = '/var/www/vhosts/geo.zrealtycorp.com/geo/media/'
MEDIA_URL = '/media/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

SITE_DOMAIN = 'geo.zrealtycorp.com'

SITE_NAME = 'geo.zrealtycorp'

STATICFILES_DIRS = (
  './static_files',
  './static_files/css',
  './static_files/css/themes',
  './static_files/js',
  './static_files/js',
  './static_files/js/angular',
  './static_files/js/require',
  './static_files/js/jquery',
  '/usr/local/lib/python2.7/site-packages/grappelli/static',
#  '/usr/local/lib/python2.7/site-packages/rest_framework/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'coffeescript.finders.CoffeescriptFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

COMPRESS_OFFLINE = True
# See the django-compressor docs at http://django_compressor.readthedocs.org/en/latest/settings/
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)


TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
     ('django_mobile.loader.CachedLoader', (
            'django_mobile.loader.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
     )),
     ('pyjade.ext.django.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
     )),

     ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
TEMPLATE_DIRS = (
    '/var/www/vhosts/zrealtycorp.com/zrealty/templates/',
    '/var/www/vhosts/zrealtycorp.com/zrealty/api/templates/',   
    '/var/www/vhosts/zrealtycorp.com/zrealty/pages/templates/',
    '/usr/local/lib/python2.7/site-packages/pinax_theme_bootstrap/templates',
    '/usr/local/lib/python2.7/site-packages/djfrontend/templates',
    '/usr/local/lib/python2.7/site-packages/sekizai/test_templates',
    '/usr/local/lib/python2.7/site-packages/bootstrap_toolkit/templates',
    '/var/www/vhosts/zrealtycorp.com/zrealty/Django-Socialauth/build/lib/socialauth/templates',
    '/usr/local/lib/python2.7/site-packages/grappelli/templates',
)
CORS_ORIGIN_ALLOW_ALL = True
# Backend to use

# User-agents to render for, if you're using the UserAgentMiddleware
# Defaults to the most popular.  If you have custom needs, pull from the full list:
# http://www.useragentstring.com/pages/Crawlerlist/

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
TEST_RUNNER = 'django_selenium.selenium_runner.SeleniumTestRunner'

FEED_UPDATE_CELERY = True

PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)

DEFAULT_INDEX_TABLESPACE = ''
CSS_URL = '/var/www/vhosts/geo.zrealtycorp.com/geo/static/css'


GRAPPELLI_ADMIN_TITLE = 'Melinae'

GRAPPELLI_INDEX_DASHBOARD = {
   'django.contrib.admin.site': 'zrealty.dashboard.CustomIndexDashboard',
}
PAGING_PAGE_SIZE = 10

APPEND_SLASH = True

UPLOAD_ROOT = 'images'
#CRISPY_TEMPLATE_PACK = 'uni_form'
#TASTYPIE_ABSTRACT_APIKEY = True




