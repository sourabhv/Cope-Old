from django.contrib import admin
from opac.models import *

class BookAdmin(admin.ModelAdmin):
	# ordering and display of fields in edit/add form. Can reorder and hide fields
	fields =  ('date', 'title', 'edition', 'isbn', 'ddc', 'authors', 'publisher',
		 'publish_date', 'publish_place', 'pages', 'cost', 'source', 'imageurl', 'remarks',)

	# readonly fields in edit/add form
	readonly_fields = ('date',)

	# Order and names of fields displayed in list
	list_display = ('title', 'isbn', 'ddc', 'authors', 'publisher')

	# fields to use for search
	search_fields = ('title', 'publisher', 'isbn', 'ddc', 'author__name')

	# ordering of the list - priority wise - title > publisher > ...
	ordering = ('title', 'edition', 'isbn')

	# input type for ManyToMany field
	# filter_horizontal = ()

	# ForiegnKey fields whose input will be through their id in their table
	# raw_id_fields = ('',)

	# used to create filter on right side of page
	list_filter = ('date',)

class BookCopyAdmin(admin.ModelAdmin):
	fields = ('date', 'book_number', 'book_category', 'issued_to',)
	readonly_fields = ('date',)
	list_display = ('book_category', 'date', 'book_number', 'issued_to',)
	list_filter = ('date',)
	search_fields = ('book_number',)
	ordering = ('book_category', 'book_number',)

admin.site.register(Book, BookAdmin)
admin.site.register(BookCopy, BookCopyAdmin)
