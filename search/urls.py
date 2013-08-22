from django.conf.urls import patterns, url
# from search import views

# from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',
	url(r'^$', 'forward'),
	url(r'^search/$', 'index'),
	url(r'^search/book/(?P<book_id>\d+)', 'get_book'),
)
