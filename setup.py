import os
import sys
from setuptools import setup, find_packages

setup(
    name = 'django-notes',
    version = '0.1.0',
    description = '''Template for my django applications.''',
    keywords = 'django apps',
    license = 'New BSD License',
    author = 'Roman Dolgiy',
    author_email = 'tosters@gmail.com',
    url = 'http://github.com/t0ster/django-notes/',
    install_requires = [],
    dependency_links = [],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)

