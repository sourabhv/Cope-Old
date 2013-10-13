import os
from random import randint
if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cope.settings")

from opac.models import Book, BookCopy

def make_isbn():
	return randint(1000000000000, 9999999999999)

titles = ['Gray Hat Python', 'Introduction to Algorithms', 'Pro Python',
	'HTML5 and JavaScript Projects', 'NginX HTTP Server', 'Redis Cookbook',
	'Python Fundamentals', 'Land of Lisp', 'Beginning iOS Game Development',
	'Ruby on Rails for Dummies', 'Django, AJAX and jQuery']

authors = ['Seitz', 'Thomas H. Corman', 'Marty Alchin', 'Geanie Mayer', 'Clement',
	'Tiago Macedo', 'Kent Lee', 'Courad', 'Patrick', 'Barry Burd', 'Jonathan Hayward']

publishers = ['No Starch Press', 'Stanford Press', 'Apress', 'Apress', 'Packt OpenSource',
	'O\'Reilly', 'Springer', 'No Starch Press', 'WROK', 'For Dummies', 'Packt OpenSource']

imageurls = ['grayhat.png', 'introtoalgo.png', 'propython.png', 'htmljs.png', 'nginx.png',
	'redis.png', 'pythonfundamentals.png', 'lisp.png', 'ios.png', 'ror.png', 'djangoajax.png']

def main():
	for i in range(len(titles)):
		isbn = make_isbn()
		new_book = Book(title=titles[i], isbn=isbn, ddc=randint(100,999), authors = authors[i],
			publisher=publishers[i], cost=randint(300,700), imageurl=imageurls[i], pages=randint(300,700))
		new_book.save()
		print '\n%4d | ISBN: %s | Title: %s' % (i+1, isbn, titles[i])
		for j in range(randint(5,10)):
			book_number = randint(50000,900000)
			book_copy = BookCopy(book_number=book_number, book_category=new_book)
			book_copy.save()
			print '%10d | Book Number: %-6d | Category: %s' % (j+1, book_number, new_book.title)

if __name__ == '__main__':
	main()
