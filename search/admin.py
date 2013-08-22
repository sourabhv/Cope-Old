from django.contrib import admin
from search.models import Book, Author, Enduser, IssuedBook, Student, Employee

class BookAdmin(admin.ModelAdmin):
	# Order and names of fields displayed in list
	list_display = ('title', 'isbn', 'ddc', 'authors', 'publisher')

	# fields to use for search
	search_fields = ('title', 'publisher', 'isbn', 'ddc', 'author__name')

	# ordering of the list - priority wise - title > publisher > ...
	ordering = ('title', 'edition', 'isbn')

	# input type for ManyToMany field
	filter_horizontal = ('author',)

	# ForiegnKey fields whose input will be through their id in their table
	# raw_id_fields = ('',)

	# used to create filter on right side of page
	list_filter = ('date',)

	# ordering and display of fields in edit form. Can reorder and hide fields
	# fields = ('',)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'website')
	search_fields = ('name', 'website')
	ordering = ('name',)

class EnduserAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		# Return empty perms dict thus hiding the model from admin index.
		return {}

class StudentAdmin(admin.ModelAdmin):
	fields = ('name', 'rollno', 'branch', 'course', 'year', 'booklimit', 'dues', 'book')
	list_display = ('name', 'rollno', 'course', 'dues')
	list_filter = ('course', 'branch', 'year')
	search_fields = ('name', 'rollno')
	ordering = ('rollno',)
	filter_horizontal = ('book',)
	list_filter = ('course', 'branch', 'year')

class EmployeeAdmin(admin.ModelAdmin):
	fields = ('employee_id', 'name', 'booklimit', 'dues', 'book')
	list_display = ('employee_id', 'name')
	list_filter = ('employee_id', 'name')
	search_fields = ('employee_id', 'name')
	ordering = ('name', 'employee_id')
	filter_horizontal = ('book',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Enduser, EnduserAdmin)
admin.site.register(IssuedBook)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee, EmployeeAdmin)
