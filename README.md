Cope
====

A digital library tool comprising of a public access view and equipped with fully functioning administrative tasks such as cataloging and circulation of books.

Requirements
============

- Python 2.7+
- Django 1.5.1+

Getting Started
===============

- clone the repository
- run `python manage.py syncdb`
- run `python populate_book.py`
- run `python populate_student.py`
- run `python populate_employeech.py`
- run `python manage.py runserver` to start the server
- go to `localhost:8000/search` and `localhost:8000/transactions` from any modern browser.
