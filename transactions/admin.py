from django.contrib import admin
from transactions.models import *

class EndUserAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        '''
        Return empty perms dict thus hiding the model from admin index.
        '''
        return {}

class StudentAdmin(admin.ModelAdmin):
	fields = ('name', 'card_number', 'gender', 'phone_number', 'roll_number', 'branch', 'batch', 'semester',)
	list_display = ('name', 'roll_number', 'branch')
	list_filter = ('branch', 'batch', 'semester',)
	search_fields = ('name', 'rollno', 'phone_number',)
	ordering = ('name', 'roll_number')

class EmployeeAdmin(admin.ModelAdmin):
	fields = ('name', 'card_number', 'gender', 'phone_number', 'employee_id', 'joining_date', 'department', 'designation',)
	list_display = ('name', 'employee_id', 'department', 'designation')
	list_filter = ('joining_date', 'department', 'designation')
	search_fields = ('employee_id', 'name', 'phone_number')
	ordering = ('name', 'employee_id')

admin.site.register(EndUser, EndUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee, EmployeeAdmin)
