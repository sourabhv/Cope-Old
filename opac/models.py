from django.db import models
from django.utils import timezone
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes import generic

from transactions.models import EndUser

class Book(models.Model):
	'''
	Part of accessing register enlisting book details.
	Contains general details relative to a book e.g. title, author,
	edition, publisher etc.
	'''

	# book information
	date = models.DateField(auto_now_add=True, verbose_name='cataloguing date')
	title = models.CharField(max_length=50)
	edition = models.IntegerField(default=1)
	isbn = models.CharField(max_length=13, verbose_name='ISBN')
	ddc = models.CharField(max_length=3, verbose_name='DDC')

	# author/publisher information
	authors = models.CharField(max_length=100, blank=True)
	publisher = models.CharField(max_length=50)
	publish_date = models.DateTimeField(null=True, blank=True)
	publish_place = models.CharField(max_length=50, blank=True)

	# other information
	source = models.CharField(max_length=50, blank=True)
	pages = models.IntegerField(default=0)
	cost = models.IntegerField()
	imageurl = models.CharField(max_length=50, blank=True)
	remarks = models.TextField(blank=True)

	@property
	def copies_available(self):
		return self.copies.filter(issued_to__isnull=True).count()

	def __init__(self, *args, **kwargs):
		super(Book, self).__init__(*args, **kwargs)
		if self.authors == '':
			self.authors = self.publisher

	def __unicode__(self):
		return '%s | %s' % (self.title, self.isbn)

class BookCopy(models.Model):

	date = models.DateField(auto_now_add=True, verbose_name='cataloguing date')
	book_number = models.IntegerField(verbose_name='book number')

	# Foreign keys
	book_category = models.ForeignKey(Book, related_name='copies')
	issued_to = models.ForeignKey(EndUser, related_name='issued_books', null=True, blank=True)

	# @property
	# def book_number():
	# 	pass

	# GenericForeignKey to transaction.models.EndUser Model using ContentType
	# content_type = models.ForeignKey(ContentType)
	# object_id = models.PositiveIntegerField()
	# issued_to = models.GenericForeignKey('content_type', 'object_id')
	class Meta:
		verbose_name=u'book copy'
		verbose_name_plural=u'book copies'


	def __unicode__(self):
		return 'Book Copy Number: %d' % self.book_number
