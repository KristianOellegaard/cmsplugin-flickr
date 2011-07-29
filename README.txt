Flickr Plugin for django CMS
============================

This is a flickr plugin for `django CMS`_. It enables you to display Flickr images on your pages, getting them by username, group-id or tags!

Installation
------------

 * Put it somewhere on your ``PYTHONPATH`` (with virtualenv+pip, Buildout, ...)
 * The plugin requires "Beej's `Python Flickr API`_, get it from pypi.
 * Add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (..., 'cmsplugin_flickr,)

 * Run ``python manage.py syncdb``
 * Obtain a Flickr API key at Flickr_.
 * Add the key and the secret to your ``settings.py``::

    FLICKR_API_KEY = 'xxxx'
    FLICKR_API_SECRET = 'xxxx'

 * Place it on a page and use it!


.. _django CMS: http://www.django-cms.org
.. _Python Flickr API: http://stuvel.eu/projects/flickrapi
.. _Flickr: http://www.flickr.com/services/apps/create/apply