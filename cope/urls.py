from django.conf.urls import patterns, include, url
# from search.views import viewname
from cope import settings

from django.contrib import admin
admin.autodiscover()

# Setup Brillixy views & templates
# import brillixy.site
# brillixy.site.setup(admin.site)

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	(r'^grappelli/', include('grappelli.urls')),
	url(r'^', include('search.urls', namespace="search")),
)
