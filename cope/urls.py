from django.conf.urls import patterns, include, url
from cope import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),

	url(r'^', include('opac.urls', namespace="opac")),
)
