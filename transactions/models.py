from datetime import datetime
from django.db import models

class EndUser(models.Model):
	'''
	Part of accessing register enlisting EndUser details.
	Inherited by Student and Employee Models.

	Contains common user specific details - name, card_number, gender,
	phone_number.
	'''

	gender_choices = (
		(u'F', u'Female'),
		(u'M', u'Male'),
		(u'U', u'Unspecified'),
	)

	name = models.CharField(max_length=50)
	card_number = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=gender_choices,)
	phone_number = models.CharField(max_length=15)

class Student(EndUser):
	'''
	Student peculiar schema.
	comprises of details kin to student and book issue details.
	'''

	roll_number = models.CharField(max_length=20)
	branch = models.CharField(max_length=30)
	batch = models.CharField(max_length=4, default = datetime.now().year)
	semester = models.CharField(max_length=1)

	def __unicode__(self):
		return '%s | %s' % (self.name, self.roll_number)

class Employee(EndUser):
	'''
	Employee or faculty peculiar schema.
	comprises of details kin to employee and book issue details.
	'''

	employee_id = models.CharField(max_length=25)
	joining_date = models.DateField()
	department = models.CharField(max_length=50)
	designation = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s | %s' %(self.name, self.employee_id)
