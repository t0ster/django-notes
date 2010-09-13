Introduction
============

Short introduction of this django_ project.

Runing Example Project
----------------------

::

	git clone git://github.com/t0ster/django-notes.git
	cd django-notes
	python bootstrap.py
	./bin/buildout
	./bin/django syncdb
	./bin/django build_static
	./bin/django runserver
	
Go to http://localhost:8000

Dependencies
------------

What is project depends on.

Installation
------------

* Add application ``django_notes`` to the ``INSTALLED_APPS`` list.
* Run ``./manage.py syncdb`` to create all neccessary tables.
* Add these variables to the settings.py::

        APP_MESSAGE = 'blah minor'

.. _django: http://djangoproject.org
