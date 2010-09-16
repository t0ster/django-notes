Introduction
============

Pluggable django_ notes app.

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

Issue tracker
-------------
http://pm.bravetoasterstudio.com/projects/django-notes/issues

Dependencies
------------

django-tinymce

Installation
------------

* Add applications ``django_notes`` and ``tinymce`` to the ``INSTALLED_APPS`` list.
* Run ``./manage.py syncdb`` to create all neccessary tables.
* Add these variables to the settings.py::

        TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")

.. _django: http://djangoproject.org
