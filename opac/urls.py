from django.conf.urls import patterns, url

urlpatterns = patterns('opac.views',
	url(r'^$', 'forward'),
	url(r'^search/$', 'index'),
	url(r'^search/book/(?P<book_id>\d+)', 'get_book'),
)
