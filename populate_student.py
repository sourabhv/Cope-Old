import os, string
from random import randint, choice

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cope.settings")

from transactions.models import Student

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

branches = ['M.tech Electronics', 'Mechanical Engineering', 'Mechanical Engg. Technology',
	'Mechanical Engineering Evening', 'Computer Science & Engg.', 'IT', 'Master In Computer Application',
	'MBA', 'Mech. Technician Toolmakig', 'Electronics & Comm. Engg.', 'M.tech Computer Science',
	'Computer Science  Engg.evening', 'Electronics Engg.evening']

def lipsum_name():
	a, b = lipsum[randint(0,len(lipsum)-1)], lipsum[randint(0,len(lipsum)-1)]
	return a + ' ' + b

def roll_number():
	 return ''.join(choice(string.lowercase) for i in range(15))

def get_gender():
	if randint(0,1): return 'M'
	return 'F'

def get_branch(): return branches[randint(0,len(branches)-1)]

def main():
	records_count = raw_input('Enter number of Student records to be added: ')
	records_count = int(records_count)
	for i in range(records_count):
		rollno = roll_number()
		name = lipsum_name()
		Student.objects.create(name=name, card_number=rollno, gender=get_gender(),
			phone_number=randint(9000000000,9999999999), roll_number=rollno,
			branch=get_branch(), batch='2013', semester=randint(1,4))
		print '%5d | Added record for %s - %s' % (i+1, name, rollno)

if __name__ == '__main__':
	main()
