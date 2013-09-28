import re

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

from opac.models import *

def forward(request):
	return HttpResponseRedirect('search/')

def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	''' Splits the query string in invidual keywords.

		Also removes unecessary spaces and grouping quoted words together.
		returns a list of keywords
		Example:
		>>> normalize_query('  some random  words "with   quotes  " and   spaces')
		['some', 'random', 'words', 'with quotes', 'and', 'spaces']
	'''
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	''' Returns a query, that is a combination of Q objects. That combination
		aims to search keywords within a model by testing the given search fields.

	'''
	# Query to search for every search term
	query = None
	terms = normalize_query(query_string)
	for term in terms:
		# Query to search for a given term in each field
		term_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if term_query is None:
				term_query = q
			else:
				term_query = term_query | q
		if query is None:
			query = term_query
		else:
			query = query | term_query
	return query


def index(request):
	bookexists = False
	query_string = ''

	if 'q' in request.GET and request.GET['q']:
		query_string = request.GET['q']

		query_list = get_query(query_string, ['title', 'publisher','author__name'])

		book_list = Book.objects.filter(query_list).order_by('title')

		if book_list:
			bookexists = True

		return render (request, 'opac/search_results.html', {
			'books': book_list,
			'q': query_string,
			'bookexists': bookexists
		})

	else:
		return render(request, 'opac/search.html')

def get_book(request, book_id):
	book = Book.objects.get(pk=book_id)
	return render(request, 'opac/book_details.html', {'book' : book})