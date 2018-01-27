Enable a message on every page load.

> Looking For Authors!  This project is currently looking for a user to take it over.  If that sounds like you, send a note to derek at stegelman dot com or open up an issue in this repository.

Official Docs
-------------

http://django-site-notifications.readthedocs.org

Install
-------

To install django-site-notifications::

	pip install django-site-notifications
	
add to installed apps::

	site_notifications

add middleware::

    'site_notifications.middleware.NotificationMiddleware',

The middleware needs to be included below the messages framework.
