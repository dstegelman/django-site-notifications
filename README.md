Enable a message on every page load.

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