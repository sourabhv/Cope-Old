from django import template
from django.core.files.storage import default_storage
import os
register = template.Library()

@register.filter(name='file_exists')
def file_exists(file_rel_path):
	path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
	if default_storage.exists(path+file_rel_path):
		return file_rel_path
	else:
		return 'image.png'
