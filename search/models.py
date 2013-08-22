from django.db import models
from django.utils import timezone
from datetime import timedelta

import datetime

class Book(models.Model):
	'''
	Part of accessing register enlisting book details.
	Contains general details relative to a book e.g. title, author,
	edition, publisher etc.
	'''
	# Fields
	date = models.DateField(auto_now_add=True, verbose_name='cataloguing date')
	isbn = models.CharField(max_length=13, verbose_name='ISBN')
	ddc = models.CharField(max_length=3, verbose_name='DDC')
	book_no = models.IntegerField(verbose_name='book number')

	title = models.CharField(max_length=50)
	edition = models.IntegerField(default=1)

	# Many To Many Field
	author = models.ManyToManyField('Author')

	publisher = models.CharField(max_length=50)
	publish_date = models.DateTimeField(null=True, blank=True)
	publish_place = models.CharField(max_length=50, blank=True)

	source = models.CharField(max_length=50)
	pages = models.IntegerField(default=0)
	cost = models.IntegerField()
	copies = models.IntegerField(default=0)
	imageurl = models.CharField(blank=True,max_length=50)

	remarks = models.TextField(blank=True)
	# keywords = models.CharField(max_length=300)

	def authors(self):
		return ', '.join([obj.name for obj in self.author.all()])

	def __unicode__(self):
		return self.title


class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=60, blank=True)
	website = models.CharField(max_length=60, blank=True)

	def __unicode__(self):
		return self.name

class Enduser(models.Model):
	'''
	Part of accessing register enlisting general enduser details.

	Contains user specific details w.r.t. membership i.e. faculty/students
	e.g. Type of user, Name, Id/Rollno., maximum book issue limit,
	dues and current issue status.

	booklimit is user_type dependent
	'''
	# Fields
	name = models.CharField(max_length=50)
	booklimit = models.IntegerField(default=0, verbose_name='book limit')
	dues = models.IntegerField(default=0)

	# Many To Many Fields
	book = models.ManyToManyField('Book', blank=True)

	def __unicode__(self):
		return self.name

class Student(Enduser):
	'''
	Student peculiar schema.
	comprises of details kin to student and book issue details.
	'''
	COURSES = (
		(u'1', u'B.Tech'),
		(u'2', u'M.Tech'),
		(u'3', u'BBA'),
		(u'4', u'MBA'),
	)

	rollno = models.CharField(max_length=20, verbose_name='roll number')
	branch = models.CharField(max_length=20)
	course = models.CharField(max_length=20, choices=COURSES)
	year = models.IntegerField()

	def book_limit(self):
		pass

class Employee(Enduser):
	'''
	Employee or faculty peculiar schema.
	comprises of details kin to employee and book issue details.
	'''

	employee_id = models.CharField(max_length=20, verbose_name='employee ID')

	def book_limit(self):
		pass

class IssuedBook(models.Model):
	'''
	Files the circulation of books and patrons.
	'''

	# Foreign Keys
	book = models.ForeignKey(Book)
	enduser = models.ForeignKey(Enduser)
	# Fields
	issued_copies = models.IntegerField(default=0)

	def currently_available(self):
		# returns the number of available copies of a book if any.
		pass
