import re
from StringIO import StringIO

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
# from django.core import serializers
from django.core.serializers.json import Serializer

from opac.models import Book, BookCopy

class JSONSerializer(Serializer):
	'''
	JSON serialize to serialize db fields and properties

	Example:
	>>> JSONSerializer().serialize(Model.objects.all(), ('field1', 'field2',))
	'''
	def serialize(self, queryset, attributes, **options):
		self.options = options
		self.stream = options.get("stream", StringIO())
		self.start_serialization()
		self.first = True

		for obj in queryset:
			self.start_object(obj)
			for field in attributes:
				self.handle_field(obj, field)
			self.end_object(obj)
			if self.first:
				self.first = False
		self.end_serialization()
		return self.getvalue()

	def handle_field(self, obj, field):
		self._current[field] = getattr(obj, field)


def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	'''
	Splits the query string in invidual keywords.

	Also removes unecessary spaces and grouping quoted words together.
	returns a list of keywords
	Example:
	>>> normalize_query('  some random  words "with   quotes  " and   spaces')
	['some', 'random', 'words', 'with quotes', 'and', 'spaces']
	'''
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	'''
	Returns a query, that is a combination of Q objects. That combination
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

def forward(request):
	return HttpResponseRedirect('search/')

def index(request):
	query_string = request.GET.get('q', '')
	spaces = re.compile(r'[ \t]+')
	if query_string != '':
		if request.is_ajax():
			opac_fields = ('title', 'edition', 'isbn', 'authors', 'publisher',
				'pages', 'imageurl', 'remarks', 'copies_available',)
			serializer = JSONSerializer()
			if spaces.match(query_string):
				books_json = '[]'
			elif query_string == 'opac.models.Book --all':
				books = Book.objects.all().order_by('title')
				books_json = serializer.serialize(books, attributes=opac_fields)
			else:
				query_list = get_query(query_string, ['title', 'publisher','authors'])
				books = Book.objects.filter(query_list).order_by('title')
				books_json = serializer.serialize(books, attributes=opac_fields)

			return HttpResponse(books_json, content_type='application/json')

		else:
			query_list = get_query(query_string, ['title', 'publisher','authors'])
			books = Book.objects.filter(query_list).order_by('title')
			return render(request, 'opac/search.html', {
				'q': query_string,
				'books': books
			})
	else:
		return render(request, 'opac/search.html')

# def index(request):
# 	query_string = request.GET.get('q', '')
# 	spaces = re.compile(r' +')
# 	if query_string != '':
# 		opac_fields = ('title', 'edition', 'isbn', 'authors', 'publisher',
# 			'pages', 'imageurl', 'remarks', 'copies_available',)
# 		if spaces.match(query_string):
# 			books_json = '[]'
# 		elif query_string == 'opac.models.Book --all':
# 			books = Book.objects.all().order_by('title')
# 			books_json = serializers.serialize('json', books, fields=opac_fields)
# 		else:
# 			query_list = get_query(query_string, ['title', 'publisher','authors'])
# 			books = Book.objects.filter(query_list).order_by('title')
# 			books_json = serializers.serialize('json', books, fields=opac_fields)

# 		return HttpResponse(books_json, content_type='application/json')
# 	else:
# 		return render(request, 'opac/search.html')

def get_book(request, book_id):
	book = Book.objects.get(pk=book_id)
	return render(request, 'opac/book_details.html', {'book' : book})
