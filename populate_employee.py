import os, string, datetime
from random import randint, choice

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cope.settings")

from transactions.models import Employee

lipsum = ['accumsan', 'adipiscing', 'aenean', 'aliquam', 'aliquet', 'amet',
'ante', 'aptent', 'arcu', 'at', 'auctor', 'augue', 'bibendum', 'blandit', 'class',
'commodo', 'condimentum', 'congue', 'consectetuer', 'consequat', 'conubia', 'convallis',
'cras', 'cubilia', 'cum', 'curabitur', 'curae', 'cursus', 'dapibus', 'diam', 'dictum',
'dictumst', 'dignissim', 'dis', 'dolor', 'donec', 'dui', 'duis', 'egestas', 'eget',
'eleifend', 'elementum', 'elit', 'eni', 'enim', 'erat', 'eros', 'est', 'et', 'etiam',
'eu', 'euismod', 'facilisi', 'facilisis', 'fames', 'faucibus', 'felis', 'fermentum',
'feugiat', 'fringilla', 'fusce', 'gravida', 'habitant', 'habitasse', 'hac', 'hendrerit',
'hymenaeos', 'iaculis', 'id', 'imperdiet', 'in', 'inceptos', 'integer', 'interdum', 'ipsum',
'justo', 'lacinia', 'lacus', 'laoreet', 'lectus', 'leo', 'libero', 'ligula', 'litora',
'lobortis', 'lorem', 'luctus', 'maecenas', 'magna', 'magnis', 'malesuada', 'massa',
'mattis', 'mauris', 'metus', 'mi', 'molestie', 'mollis', 'montes', 'morbi', 'mus', 'nam',
'nascetur', 'natoque', 'nec', 'neque', 'netus', 'nibh', 'nisi', 'nisl', 'non', 'nonummy',
'nostra', 'nulla', 'nullam', 'nunc', 'odio', 'orci', 'ornare', 'parturient', 'pede',
'pellentesque', 'penatibus', 'per', 'pharetra', 'phasellus', 'placerat', 'platea', 'porta',
'porttitor', 'posuere', 'potenti', 'praesent', 'pretium', 'primis', 'proin', 'pulvinar',
'purus', 'quam', 'quis', 'quisque', 'rhoncus', 'ridiculus', 'risus', 'rutrum', 'sagittis',
'sapien', 'scelerisque', 'sed', 'sem', 'semper', 'senectus', 'sit', 'sociis', 'sociosqu',
'sodales', 'sollicitudin', 'suscipit', 'suspendisse', 'taciti', 'tellus', 'tempor', 'tempus',
'tincidunt', 'torquent', 'tortor', 'tristique', 'turpis', 'ullamcorper', 'ultrices', 'ultricies',
'urna', 'ut', 'varius', 've', 'vehicula', 'vel', 'velit', 'venenatis', 'vestibulum', 'vitae',
'vivamus', 'viverra', 'volutpat', 'vulputate']

def lipsum_name():
	a, b = lipsum[randint(0,len(lipsum)-1)], lipsum[randint(0,len(lipsum)-1)]
	return a + ' ' + b

def randstr(l):
	 return ''.join(choice(string.lowercase) for i in range(l))

def get_gender():
	if randint(0,1): return 'M'
	return 'F'

def main():
	records_count = raw_input('Enter number of Employee records to be added: ')
	records_count = int(records_count)
	for i in range(records_count):
		name = lipsum_name()
		empno = randstr(15)

		Employee.objects.create(name=name, card_number=empno, gender=get_gender(),
			phone_number=randint(9000000000,9999999999), joining_date=datetime.datetime.now(),
			employee_id=empno, department=randstr(10), designation='Unspecified')
		print '%5d | Added record for %s - %s' % (i+1, name, empno)

if __name__ == '__main__':
	main()
