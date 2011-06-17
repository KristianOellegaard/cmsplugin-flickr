from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'cmsplugin-flickr',
    version = version,
    description = 'flickr plugin for django-cms',
    author = 'Bernhard Vallant',
    author_email = '',
    packages = find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=1.2',
        'django-cms',
		'flickrapi',
    ],
)